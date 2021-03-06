__title__ = 'Vanish'
__author__ = 'Jakkee'
__version__ = '1.0.2'

import clr
clr.AddReferenceByPartialName("Fougerite")
import Fougerite


class Vanish:
    def On_Command(self, Player, cmd, args):
        if cmd == "vanish":
            if Plugin.GetIni("Settings").GetSetting("Config", "Enabled") == 'true':
                if Player.Admin or self.isMod(Player.SteamID):
                    if Player.PlayerClient.controllable.health == 0.0:
                        Player.PlayerClient.controllable.health = 100
                        Player.Notice("Players can now see you again!")
                    else:
                        Player.PlayerClient.controllable.health = (Player.PlayerClient.controllable.health - Player.PlayerClient.controllable.health)
                        Player.Notice("Players can not see you now")
                else:
                    Player.Message("You are not allowed to use this command!")
            else:
                Player.Message("Plugin has been disabled")

    def On_PluginInit(self):
        Util.ConsoleLog(__title__ + " by " + __author__ + " Version: " + __version__ + " loaded.", False)
        if not Plugin.IniExists("Settings"):
            Plugin.CreateIni("Settings")
            ini = Plugin.GetIni("Settings")
            ini.AddSetting("Config", "Enabled", "true")
            ini.AddSetting("Config", "ModeratorsCanUse", "true")
            ini.Save()

    def isMod(self, id):
        if DataStore.ContainsKey("Moderators", id):
            if Plugin.GetIni("Settings").GetSetting("Config", "ModeratorsCanUse") == "true":
                return True
            else:
                return False
        else:
            return False
