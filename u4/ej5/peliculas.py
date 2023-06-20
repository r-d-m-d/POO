
class Pelicula:

    def __init__(self, **kwargs):
        self.__adult = kwargs['adult']
        self.__backdrop_path = kwargs['backdrop_path']
        self.__genre_ids = kwargs['genre_ids']
        self.__id = kwargs['id']
        self.__original_language = kwargs['original_language']
        self.__original_title = kwargs['original_title']
        self.__overview = kwargs['overview']
        self.__popularity = kwargs['popularity']
        self.__poster_path = kwargs['poster_path']
        self.__release_date = kwargs['release_date']
        self.__title = kwargs['title']
        self.__video = kwargs['video']
        self.__vote_average = kwargs['vote_average']
        self.__vote_count = kwargs['vote_count']

    def adult(self, adult=None):
        if adult is not None:
            self.__adult = adult
        return self.__adult

    def backdrop_path(self, backdrop_path=None):
        if backdrop_path is not None:
            self.__backdrop_path = backdrop_path
        return self.__backdrop_path

    def genre_ids(self, genre_ids=None):
        if genre_ids is not None:
            self.__genre_ids = genre_ids
        return self.__genre_ids

    def id(self, id=None):
        if id is not None:
            self.__id = id
        return self.__id

    def original_language(self, original_language=None):
        if original_language is not None:
            self.__original_language = original_language
        return self.__original_language

    def original_title(self, original_title=None):
        if original_title is not None:
            self.__original_title = original_title
        return self.__original_title

    def overview(self, overview=None):
        if overview is not None:
            self.__overview = overview
        return self.__overview

    def popularity(self, popularity=None):
        if popularity is not None:
            self.__popularity = popularity
        return self.__popularity

    def poster_path(self, poster_path=None):
        if poster_path is not None:
            self.__poster_path = poster_path
        return self.__poster_path

    def release_date(self, release_date=None):
        if release_date is not None:
            self.__release_date = release_date
        return self.__release_date

    def title(self, title=None):
        if title is not None:
            self.__title = title
        return self.__title

    def video(self, video=None):
        if video is not None:
            self.__video = video
        return self.__video

    def vote_average(self, vote_average=None):
        if vote_average is not None:
            self.__vote_average = vote_average
        return self.__vote_average

    def vote_count(self, vote_count=None):
        if vote_count is not None:
            self.__vote_count = vote_count
        return self.__vote_count

    def __str__(self):
        p18 = "+18" if self.__adult else ""
        return f'{p18}  {self.__backdrop_path}  {self.__genre_ids}  {self.__id}  {self.__original_language}  {self.__original_title}  {self.__overview}  {self.__popularity}  {self.__poster_path}  {self.__release_date}  {self.__title}  {self.__video}  {self.__vote_average}  {self.__vote_count}'

class ManejaPelicula:

    def __init__(self, results):
        self.__pelis = []
        for dpeli in results:
            opeli = Pelicula(**dpeli)
            self.__pelis.append(opeli)

    def enlistartTitulos(self, cb):
        for p in self.__pelis:
            cb(p.title())

    def muestra_pelis(self):
        return [f'{peli}' for peli in self.__pelis]

    def obtenerDescripcion(self, pos, ag):
        return [self.__pelis[pos].title(),
                self.__pelis[pos].original_language(),
                self.__pelis[pos].release_date(),
                ag.obtenerGenerosStr(self.__pelis[pos].genre_ids()),
                self.__pelis[pos].overview()]


if __name__ == "__main__":
    pelis = ManejaPelicula().muestra_pelis()
    for peli in pelis:
        print(peli)
