"""utils.export
---

Exports the plots as interactive html
"""
import logging
import os

log = logging.getLogger("MetaStalk")


def export(choice: str, output_dir: str, plots: dict):
    """export

    Exports the plots to the chosen format

    Arguments:
        choice {str}: -- The type of export. {html, pdf, svg, png}
        output_dir {str} -- Name of the directory to output charts to.
        plots {dict} -- The plots to export.
    """
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    else:
        if len(os.listdir(output_dir)) != 0:
            log.warning("The chosen output directory contain files.")

    if choice == "html":
        for name, chart in plots.items():
            chart.write_html(f"{output_dir}/{name}.html")
    elif choice in ["pdf", "svg", "png"]:
        try:
            for name, chart in plots.items():
                chart.write_image(f"{output_dir}/{name}.{choice}")
        except ValueError:
            log.error("Dash requires orca to be install to export images.")
            raise EnvironmentError("Dash requires orca to be install to export images.")
