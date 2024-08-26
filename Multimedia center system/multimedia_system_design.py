from abc import ABC, abstractmethod

class Description:
    def __init__(self, description) -> None:
        self.__description = description
        
    def get_description(self):
        return self.__description

    

class Media(ABC):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        
    @abstractmethod
    def play(self):
        pass
        
class Music(Description,Media):
    def __init__(self, title, duration, description):
        Description.__init__(self,description)
        Media.__init__(self, title, duration)
    
    def play(self):
        print(f"Playing music: {self.title}")
        
    def info(self):
        print(f"Music title: {self.title}, Music Description: {self.get_description()}, Duration: {self.duration}")
        
        
class Video(Description,Media):
    def __init__(self, title, duration, description):
        Description.__init__(self,description)
        Media.__init__(self, title, duration)
    
    def play(self):
        print(f"Playing Video: {self.title}")
        
    def info(self):
        print(f"Video title: {self.title}, Video Description: {self.get_description()}, Duration: {self.duration}")
        

class AudioBook(Description,Media):
    def __init__(self, title, duration, description):
        Description.__init__(self,description)
        Media.__init__(self, title, duration)
    
    def play(self):
        print(f"Playing Audiobook: {self.title}")
        
    def info(self):
        print(f"Audiobook title: {self.title}, Audiobook Description: {self.get_description()}, Duration: {self.duration}")
        
class Library:
    def __init__(self):
        self.__media_items = []
        self.__media_by_genre = {}
        self.__genre = ""
        
    def get_media_by_genre(self):
        return self.__media_by_genre
        
    def add_media(self, media):
        if isinstance(media, Music):
            self.__genre = 'Music'
        elif isinstance(media, Video):
            self.__genre = "Video"
        elif isinstance(media, AudioBook):
            self.__genre = "Audiobook"
            
        if self.__genre in self.__media_by_genre:
            self.__media_by_genre[self.__genre].append(media)
        else:
            self.__media_by_genre[self.__genre] = [media,]
   
            
        
    def get_media_items(self):
        return self.__media_items
    
class MediaPlayer:
    def play_media(self, media):
        media.play()

class User(ABC):
    def __init__(self, name):
        self.__name = name
    
    @abstractmethod
    def play_media(self):
        pass
        
        
class FreeUser(User):
    def __init__(self, name):
        super().__init__(name)
    
    def play_media(self, library):
        for media in library.get_media_items():
            print(media.info())
            
class PremiumUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.__favourite_genre = None
        
    def play_media(self, library):
        # for media in library.get_media_items():
        #     if isinstance(media, Music) and self.__favourite_genre == 'Music':
        #         media.info()
        #     elif isinstance(media, Video) and self.__favourite_genre == 'Video':
        #         media.info()
        #     elif isinstance(media, AudioBook) and self.__favourite_genre == 'Audiobook':
        #         media.info()
        
        if self.__favourite_genre in library.get_media_by_genre():
            for media in library.get_media_by_genre()[self.__favourite_genre]:
                media.info()

            
        
    def set_favorite_genre(self, genre):
        self.__favourite_genre = genre
    
    def get_favorite_genre(self):
        return self.__favourite_genre
    
        
        
        

# add media to library
library = Library()

music = Music("The music", 3.56, "This is description")
music2 = Music("The music 2", 3.56, "This is description")
video = Video("The Video", 50.56, "This is video description")
audiobook = AudioBook("The Audio Book", 50.56, "This is Audiobook description")

library.add_media(music)
library.add_media(music2)
library.add_media(video)
library.add_media(audiobook)



premium_user = PremiumUser("John")
premium_user.set_favorite_genre("Music")

premium_user.play_media(library)
# print(isinstance(premium_user, User))

free_user = FreeUser("Alex")
# free_user.play_media(library)

player = MediaPlayer()

# for media in library.get_media_items():
#     player.play_media(media)