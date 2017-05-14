import asset_definitions
import django.forms


def test_js():
    media = asset_definitions.Media(
        js=(
            "foo.js",
        )
    )
    assert media.render() == media["js"].render() == (
        """<script type="text/javascript" src="/static/foo.js"></script>"""
    )

    media.add_js((
        "foo.js",
        "bar.js",
    ))

    assert media.render() == media["js"].render() == (
        """<script type="text/javascript" src="/static/foo.js"></script>\n"""
        """<script type="text/javascript" src="/static/bar.js"></script>"""
    )


def test_css():
    media = asset_definitions.Media(
        css={
            "all": (
                "all.css",
            ),
            "print": (
                "print.css",
            )
        }
    )
    assert media.render() == media["css"].render() == (
        """<link href="/static/all.css" type="text/css" media="all" rel="stylesheet" />\n"""
        """<link href="/static/print.css" type="text/css" media="print" rel="stylesheet" />"""
    )

    media.add_css({
        "all": (
            "all.css",
            "foo.css",
        )
    })

    assert media.render() == media["css"].render() == (
        """<link href="/static/all.css" type="text/css" media="all" rel="stylesheet" />\n"""
        """<link href="/static/foo.css" type="text/css" media="all" rel="stylesheet" />\n"""
        """<link href="/static/print.css" type="text/css" media="print" rel="stylesheet" />"""
    )


def test_combined():
    media_1 = asset_definitions.Media(
        js=(
            "foo.js",
        )
    )
    media_2 = asset_definitions.Media(
        css={
            "all": (
                "all.css",
            ),
        }
    )
    combined_media = media_1 + media_2
    assert combined_media.render() == (
        """<link href="/static/all.css" type="text/css" media="all" rel="stylesheet" />\n"""
        """<script type="text/javascript" src="/static/foo.js"></script>"""
    )


def test_combine_with_django_forms_media():
    assets_definition_media = asset_definitions.Media(
        js=(
            "foo.js",
        )
    )
    django_forms_media = django.forms.Media(
        js=(
            "foo.js",
            "bar.js",
        )
    )
    combined_media = assets_definition_media + django_forms_media
    assert combined_media.render() == (
        """<script type="text/javascript" src="/static/foo.js"></script>\n"""
        """<script type="text/javascript" src="/static/bar.js"></script>"""
    )
