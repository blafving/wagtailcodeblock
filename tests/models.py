from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.blocks import StreamBlock
from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from wagtailcodeblock.blocks import CodeBlock


class ContentStreamBlock(StreamBlock):
    """
    Test StreamBlock with a CodeBlock.
    """
    code = CodeBlock()


class TestPage(Page):
    body = StreamField(
        ContentStreamBlock(),
        blank=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
