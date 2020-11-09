from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.TeamGameroomDataMessage import TeamGameroomDataMessage

from Utils.Reader import BSMessageReader


class TeamUseGadgetMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.useGadget = self.read_Vint()

    def process(self):
        TeamGameroomDataMessage(self.client, self.player).send()