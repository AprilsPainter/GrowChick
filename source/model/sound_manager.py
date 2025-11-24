"""사운드 기능 관리"""
# source/model/sound_manager.py

import os
import pygame as py


class SoundManager:    
    _instance = None

    @staticmethod
    def get_instance():
        if SoundManager._instance is None:
            SoundManager()
        return SoundManager._instance

    def __init__(self):
        if SoundManager._instance is not None:
            return
        py.mixer.init()

        self.sounds = {}
        self.bgm = {}
        self.sound_volume = 1.0
        self.bgm_volume = 1.0

        SoundManager._instance = self
    
    def load_sound(self, name: str, path: str):
        sound = py.mixer.Sound(path)
        sound.set_volume(self.sound_volume)
        self.sounds[name] = sound
    
    def play_sound(self, name: str):
        if name in self.sounds:
            self.sounds[name].play()
    
    def play_bgm(self, path: str, loops: int = -1, fade_ms: float = 1500):
        if os.path.exists(path):
            py.mixer.music.load(path)
            py.mixer.music.set_volume(self.music_volume)
            py.mixer.music.play(loops, fade_ms=fade_ms)

    def stop_bgm(self, fade_ms: float = 1500):
        py.mixer.music.fadeout(fade_ms)
    
    def set_sound_volume(self, value: float):
        self.sound_volume = value
        for s in self.sounds.values():
            s.set_volume(value)
    
    def set_bgm_volume(self, value: float):
        self.bgm_volume = value
        py.mixer.music.set_volume(value)
