import logging
import os
if os:
    try:
        os.remove("launcher.log")
    except:
        pass

import sys
if sys:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(filename="launcher.log",
                        level=logging.DEBUG, format=FORMAT)

      
import justpy as jp
import ofjustpy as oj
import ofjustpy_react as ojr
from tailwind_tags import *


def render_nav_bar(session_manager):
    with session_manager.uictx("navbar") as navbarCtx:

        # a box placed at the  right end
        right_nav_box_ = oj.Halign_(oj.StackH_("anchors",
                                              cgens = [
                                                  oj.A_("active", href="#", text="Active"),
                                                  oj.A_("link", href="#", text="link"),
                                                  oj.A_("docs", href="#", text="docs"),
                                              ]
                                               ),
                                    "end"
                                   )

        #oj.Halign_(oj.Span_("dummySpan", text="i am a dummy span", pcp=[bg/pink/2])),
        cgens = [
            oj.A_("HomeAnchor", pcp=[fc/gray/9, fz.xl, fw.extrabold],
                  href="#", text="Minimal Blog"),

             right_nav_box_ 
        ]
        abox_ = oj.StackH_("abox", cgens = cgens, pcp=[pd/y/4,  ji.center, jc.between])
        oj.Nav_("panel", cgens=[abox_])
            

def render_content_body(session_manager):
    with session_manager.uictx("contentbody") as contentbodyCtx:
        apara = oj.Prose_("apara",  text="The basic blog page layout is available and all using the default Tailwind CSS classes (although there are a few hardcoded style tags). If you are going to use this in your project, you will want to convert the classes into components.")
        oj.Subsection_("panel", "I am heading", apara, pcp=[mr/st/8])


    pass

def render_footer(session_manager):
    with session_manager.uictx("footerbody") as footerbodyCtx:
        _ictx = footerbodyCtx
        oj.Prose_("aboutcontent",
                  text= "12Vcomputing focuses on desktop and server computing over low powered hardware, primarily Raspberry Pis and mobile devices. The site is maintained by Kabira", pcp=[fz.sm, text/gray/600, pd/y/2])

        oj.Subsection_("about", "About", _ictx.aboutcontent)

        oj.StackG_("linkouthref", num_cols=3, cgens = [oj.A_("link1", text="Social Link 1", href="#"),
                                        oj.A_("link2", text="Social Link 2", href="#"),
                                        oj.A_("link2", text="Social Link 3", href="#")
        ])
        oj.Subsection_("linkout", "Social/Contacts", _ictx.linkouthref)
        
        oj.Footer_("footer", cgens=[oj.Divider_("bodyFooterDivider", pcp=[mr/sb/4]),
                                    oj.StackH_("boxcontainer", cgens= [_ictx.about, _ictx.linkout]
                                        )
                                    ]
                   
                   )
        # place it at the bottom
        oj.StackH_("panel", cgens = [_ictx.footer],
                   pcp=[ppos.absolute, bottom/0, container]
                   )
@jp.SetRoute('/basic_blog')
def wp_basic_blog(request):
    session_id = request.session_id
    session_manager = oj.get_session_manager(session_id)
    stubStore = session_manager.stubStore
    with oj.sessionctx(session_manager):
        with session_manager.uictx("blogpage") as blogpageCtx:
            _ictx = blogpageCtx
            # a box shifted to the right end
            render_nav_bar(session_manager)
            render_content_body(session_manager)
            render_footer(session_manager)
            oj.Container_("tlc",
                          cgens = [_ictx.navbar.panel,
                                   _ictx.contentbody.panel,
                                   
                                   _ictx.footerbody.panel],
                          pcp=[H/"screen", bg/gray/"100/20"])
            #oj.Container_("tlc", cgens = [_ictx.contentbody.content], pcp=[H/"screen", bg/pink/1])
            wp = oj.WebPage_("wp_basic_blog",
                         cgens= [blogpageCtx.tlc],
                         template_file='svelte.html',
                             title="a svelte page")()

    wp.session_manager = session_manager

    return wp

app = jp.app
jp.justpy(wp_basic_blog, start_server=False)

# request = Dict()
# request.session_id = "abc123"
# # request.session_id = "abc123"
# wp = wp_basic_blog(request)
