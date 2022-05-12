from cmath import nan
from typing import List, Dict, Tuple
import pandas as pd
from CONSTANT import *


class Paper:
    conference: str = ""
    year: int = 2020
    title: str = ""
    doi: int = 0
    paper_type: str = ""
    authors: List[str] = []
    author_affiliation:str = ""
    internal_references: List[str] = []
    keywords: List[str] = []
    citation_count:int = 0
    pubs_cited: int = 0
    award: str = ""

    def __init__(self, row):
        self.conference = row["Conference"],
        self.year = int(row["Year"]),
        self.title = str(row["Title"]),
        self.doi = row["DOI"]
        self.paper_type = str(row["PaperType"]),
        self.authors = str(row["AuthorNames-Deduped"]).split(sep=";"),
        self.author_affiliation = str(row["AuthorAffiliation"]),
        self.internal_references = str(
            row["InternalReferences"]).split(sep=","),
        self.keywords = str(row["AuthorKeywords"]).split(sep=","),
        self.citation_count = int(row["XploreCitationCount"]),
        self.pubs_cited = int(row["PubsCited"]),
        self.award = str(row["Award"])
        if(type(self.conference) == tuple):
            self.conference = self.conference[0]
        if(type(self.year) == tuple):
            self.year = self.year[0]
        if(type(self.title) == tuple):
            self.title = self.title[0]
        if(type(self.paper_type) == tuple):
            self.paper_type = self.paper_type[0]
        if(type(self.authors) == tuple):
            self.authors = self.authors[0]
        if(type(self.author_affiliation) == tuple):
            self.author_affiliation = self.author_affiliation[0]
        if(type(self.internal_references) == tuple):
            self.internal_references = self.internal_references[0]
        if(self.internal_references[0] == "nan"):
            self.internal_references = []
        if(type(self.keywords) == tuple):
            self.keywords = self.keywords[0]
        if(type(self.citation_count) == tuple):
            self.citation_count = self.citation_count[0]
        if(type(self.pubs_cited) == tuple):
            self.pubs_cited = self.pubs_cited[0]
        if(type(self.award) == tuple):
            self.award = self.award[0]


class PaperGallery:
    '''
    A dictionary of Papers, which is a index of DIOs to paper
    '''

    def __init__(self):
        self.gallery: Dict[str, Paper] = {}

    def construct_gallery_from_main_dataset(self) -> None:
        datas: pd.DataFrame = pd.read_csv(MAIN_DATASET_PATH)
        for i in range(len(datas)):
            row = datas.iloc[i]
            paper = Paper(row)
            self.add(paper)

    def add(self, paper: Paper) -> None:
        if paper.doi in self.gallery:
            print(paper.doi)
            raise NameError("doi already exists in gallery", paper.doi)
        self.gallery[paper.doi] = paper

    def get(self, doi: int) -> Paper:
        if not(doi in self.gallery):
            raise NameError("doi not exists in gallery", doi)
        return self.gallery[doi]

    def to_list(self) -> List[Paper]:
        '''
        Convert the gallery to a list of papers
        '''
        return self.gallery.values()


if __name__ == "__main__":
    gallery = PaperGallery()
    gallery.construct_gallery_from_main_dataset()
    
    print(gallery.gallery['10.1109/TVCG.2018.2864827'].internal_references)
    print(gallery.gallery['10.1109/TVCG.2020.3029412'].paper_type)
