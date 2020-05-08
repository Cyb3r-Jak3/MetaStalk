"""utils.export
---

Exports the plots as interactive html
"""
import logging
import os


class export():
    """export
    ---

    Deals with the export to html and images. Probably not the best way to run everything but it
    works the best.
    """
    def __init__(self, choice: str, output_dir: str, plots: dict):
        self.log = logging.getLogger("MetaStalk")
        self.choice = choice
        self.output_dir = output_dir
        self.plots = plots
        self.directory_management()
        if choice in ["html", "html_offline"]:
            self.html_export()
        elif choice in ["pdf", "svg", "webp", "jpeg", "png"]:
            self.image_export()

    def directory_management(self):
        """directory_management
        ---
        Creates directory for output if it does not exist and if it does then it will check if there
        are already file in it.

        Arguments:
            output_dir {str} -- Name of the directory to check/create.
        """
        if not os.path.isdir(self.output_dir):
            os.makedirs(self.output_dir)
        else:
            if len(os.listdir(self.output_dir)) != 0:
                self.log.warning("The chosen output directory contain files.")

    def image_export(self):
        """image_export
        ---

        Deals with export images

        Raises:
            EnvironmentError: Raised if packages from metastalk[image] are not installed.
        """
        for name, chart in self.plots.items():
            try:
                chart.write_image(f"{self.output_dir}/{name}.{self.choice}")
            except ValueError:
                self.log.error("Missing packages from metastalk[image]")
                raise EnvironmentError("Missing packages from metastalk[image]")

    def html_export(self):
        """html_export
        ---
        Deals with export of html.
        If offline is true then there will be a script tag in the .html file making it much larger
        but if it is cdn then the html will cotain a script tag that points to
        https://cdn.plot.ly/plotly-latest.min.js
        """
        if self.choice == "html_offline":
            offline = True
        else:
            offline = "cdn"
        for name, chart in self.plots.items():
            chart.write_html(f"{self.output_dir}/{name}.html",
                             include_plotlyjs=offline,
                             )
