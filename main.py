# A버튼을 누를 때 마다 사람수가 1명씩 증가하며 화면에는 일의 자리만 보여줌. 전체 사람수은 B버튼을 누르면 됨.

def on_button_pressed_a():
    global cnt
    music.play(music.tone_playable(262, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    cnt += 1
    basic.show_number(cnt % 10)
input.on_button_pressed(Button.A, on_button_pressed_a)

# B버튼은 전체 사람수

def on_button_pressed_ab():
    global cnt
    cnt = 0
    basic.show_number(cnt)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# B버튼은 전체 사람수

def on_button_pressed_b():
    music.play(music.tone_playable(523, music.beat(BeatFraction.QUARTER)),
        music.PlaybackMode.UNTIL_DONE)
    basic.clear_screen()
    basic.show_number(cnt)
input.on_button_pressed(Button.B, on_button_pressed_b)

cnt = 0
cnt = 0
basic.show_number(cnt)
# [LED]..[더보기]의 <애니메이션 정지>를 넣으면 A버튼을 누를 때 빨리 넘길 수 있음. 조건문을 상용하지 않으면 B버튼을 눌렀을 때 숫자가 잠시 나오다가 사라지게 됨.

def on_forever():
    if input.button_is_pressed(Button.A):
        led.stop_animation()
basic.forever(on_forever)
