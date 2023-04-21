

setting_win = {
    "WIDTH": 500,
    "HEIGHT": 500
}
setting_board = {
    "WIDTH": 20,
    "HEIGHT": 300
}
setting_ball = {
    "RADIUS": 15
}
restart = {
    "RESTART_BALL": (setting_win["WIDTH"] // 2 - setting_ball["RADIUS"],
                    setting_win["HEIGHT"] // 2 - setting_ball["RADIUS"]),
    "RESTART_BOARD_LEFT": (15, 
                            setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2),
    "RESTART_BOARD_RIGHT": (setting_win["WIDTH"] - setting_board["WIDTH"] - 15, 
                            setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2)
}