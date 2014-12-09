# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1418161899.9736578
_enable_loop = True
_template_filename = '/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/gallery.tmpl'
_template_uri = 'gallery.tmpl'
_source_encoding = 'utf-8'
_exports = ['sourcelink', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('ui', context._clean_inheritance_tokens(), templateuri='crumbs.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'ui')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        ui = _mako_get_namespace(context, 'ui')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'ui')._populate(_import_ns, ['bar'])
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        photo_array = _import_ns.get('photo_array', context.get('photo_array', UNDEFINED))
        enable_comments = _import_ns.get('enable_comments', context.get('enable_comments', UNDEFINED))
        def content():
            return render_content(context)
        ui = _mako_get_namespace(context, 'ui')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        folders = _import_ns.get('folders', context.get('folders', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        crumbs = _import_ns.get('crumbs', context.get('crumbs', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(ui.bar(crumbs)))
        __M_writer('\n')
        if title:
            __M_writer('    <h1>')
            __M_writer(str(title))
            __M_writer('</h1>\n')
        if post:
            __M_writer('    <p>\n        ')
            __M_writer(str(post.text()))
            __M_writer('\n    </p>\n')
        if folders:
            __M_writer('    <ul>\n')
            for folder, ftitle in folders:
                __M_writer('        <li><a href="')
                __M_writer(str(folder))
                __M_writer('"><i\n        class="icon-folder-open"></i>&nbsp;')
                __M_writer(str(ftitle))
                __M_writer('</a></li>\n')
            __M_writer('    </ul>\n')
        if photo_array:
            __M_writer('    <ul class="thumbnails">\n')
            for image in photo_array:
                __M_writer('            <li><a href="')
                __M_writer(str(image['url']))
                __M_writer('" class="thumbnail image-reference" title="')
                __M_writer(str(image['title']))
                __M_writer('">\n                <img src="')
                __M_writer(str(image['url_thumb']))
                __M_writer('" alt="')
                __M_writer(str(image['title']))
                __M_writer('" /></a>\n')
            __M_writer('    </ul>\n')
        if site_has_comments and enable_comments:
            __M_writer('    ')
            __M_writer(str(comments.comment_form(None, permalink, title)))
            __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "gallery.tmpl", "source_encoding": "utf-8", "line_map": {"128": 28, "129": 29, "130": 29, "131": 29, "132": 29, "133": 31, "134": 33, "135": 34, "136": 34, "137": 34, "143": 137, "22": 4, "25": 3, "31": 0, "52": 2, "53": 3, "54": 4, "59": 5, "64": 36, "70": 5, "83": 7, "101": 7, "102": 8, "103": 8, "104": 9, "105": 10, "106": 10, "107": 10, "108": 12, "109": 13, "110": 14, "111": 14, "112": 17, "113": 18, "114": 19, "115": 20, "116": 20, "117": 20, "118": 21, "119": 21, "120": 23, "121": 25, "122": 26, "123": 27, "124": 28, "125": 28, "126": 28, "127": 28}, "filename": "/usr/local/lib/python3.4/dist-packages/nikola/data/themes/base/templates/gallery.tmpl"}
__M_END_METADATA
"""
