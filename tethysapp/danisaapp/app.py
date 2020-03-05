from tethys_sdk.base import TethysAppBase, url_map_maker


class Danisaapp(TethysAppBase):
    """
    Tethys app class for Danisaapp.
    """

    name = 'Danisaapp'
    index = 'danisaapp:home'
    icon = 'danisaapp/images/pluto.jpg'
    package = 'danisaapp'
    root_url = 'danisaapp'
    color = '#9F2B68'
    description = '"This is an app about myself"'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='danisaapp',
                controller='danisaapp.controllers.home'
            ),
            UrlMap(
                name='map',
                url='danisaapp/map',
                controller='danisaapp.controllers.map'
            )
        )

        return url_maps
