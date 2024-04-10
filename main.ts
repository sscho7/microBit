//  A버튼을 누를 때 마다 사람수가 1명씩 증가하며 화면에는 일의 자리만 보여줌. 전체 사람수은 B버튼을 누르면 됨.
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    cnt += 1
    basic.showNumber(cnt % 10)
})
//  B버튼은 전체 사람수
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    cnt = 0
    basic.showNumber(cnt)
})
//  B버튼은 전체 사람수
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.play(music.tonePlayable(523, music.beat(BeatFraction.Quarter)), music.PlaybackMode.UntilDone)
    basic.clearScreen()
    basic.showNumber(cnt)
})
let cnt = 0
cnt = 0
basic.showNumber(cnt)
//  [LED]..[더보기]의 <애니메이션 정지>를 넣으면 A버튼을 누를 때 빨리 넘길 수 있음. 조건문을 상용하지 않으면 B버튼을 눌렀을 때 숫자가 잠시 나오다가 사라지게 됨.
basic.forever(function on_forever() {
    if (input.buttonIsPressed(Button.A)) {
        led.stopAnimation()
    }
    
})
