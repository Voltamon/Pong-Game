import os
import json

class Json():
    def load_stat():
        script_path = os.path.abspath(__file__)
        stat_path = script_path[0 : script_path.find("Components")] + "Data\\user.json"
        stat_file = open(stat_path, "r")
        stat = json.load(stat_file)
        return stat
    
    def write_stat(stat):
        script_path = os.path.abspath(__file__)
        stat_path = script_path[0 : script_path.find("Components")] + "Data\\user.json"
        stat_file = open(stat_path, "w")
        stats = json.dumps(stat)
        stat_file.write(stats)
        
    def load_pos():
        script_path = os.path.abspath(__file__)
        util_path = script_path[0 : script_path.find("Components")] + "Data\\util.json"
        pos_file = open(util_path, "r")
        pos = json.load(pos_file)
        return pos
    
    def write_pos(pos):
        script_path = os.path.abspath(__file__)
        util_path = script_path[0 : script_path.find("Components")] + "Data\\util.json"
        pos_file = open(util_path, "w")
        ball_pos = json.dumps(pos)
        pos_file.write(ball_pos)
    
    def get_wins():
        user_stat = Json.load_stat()
        wins = user_stat["wins"]
        return wins
    
    def set_wins(wins):
        user_stat = Json.load_stat()
        if wins > 999:
            wins = 999
        user_stat["wins"] = wins
        Json.write_stat(user_stat)
    
    def get_draws():
        user_stat = Json.load_stat()
        draws = user_stat["draws"]
        return draws
    
    def set_draws(draws):
        user_stat = Json.load_stat()
        if draws > 999:
            draws = 999
        user_stat["draws"] = draws
        Json.write_stat(user_stat)
    
    def get_losses():
        user_stat = Json.load_stat()
        losses = user_stat["losses"]
        return losses
    
    def set_losses(losses):
        user_stat = Json.load_stat()
        if losses > 999:
            losses = 999
        user_stat["losses"] = losses
        Json.write_stat(user_stat)
    
    def get_ball_pos():
        ballPos = Json.load_pos()
        pos = (ballPos["x"], ballPos["y"])
        return pos
    
    def set_ball_pos(ballPos):
        pos = Json.load_pos()
        pos["x"] = ballPos[0]
        pos["y"] = ballPos[1]
        Json.write_pos(pos)
        
    def get_animate():
        ballPos = Json.load_pos()
        animate = ballPos["animate"]
        return animate
    
    def set_animate(animate):
        ballPos = Json.load_pos()
        ballPos["animate"] = animate
        Json.write_pos(ballPos)