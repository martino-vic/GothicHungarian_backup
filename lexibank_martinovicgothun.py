import pathlib

from cldfbench import Dataset as BaseDataset

class Dataset(BaseDataset):
    dir = pathlib.Path(__file__).parent
    id = "martinovicgothun"

    def cldf_specs(self):  # A dataset must declare all CLDF sets it creates.
        return super().cldf_specs()

    def cmd_download(self, args):
        """
        Download files to the raw/ directory. You can use helpers methods of `self.raw_dir`, e.g.
        """
        self.raw_dir.download("https://raw.githubusercontent.com/martino-vic/gerstnerhungarian/new/cldf/forms.csv", "hun.csv")
        self.raw_dir.download("https://raw.githubusercontent.com/martino-vic/streitberggothic/new/cldf/forms.csv", "got.csv")

        pass

    def cmd_makecldf(self, args):
        """
        Convert the raw data to a CLDF dataset.

        >>> args.writer.objects['LanguageTable'].append(...)
        """
        self.cmd_download(None)
        pass
