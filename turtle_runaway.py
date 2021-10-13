# This example is not working in Spyder directly (F5 or Run)
# Please type '!python turtle_runaway.py' on IPython console in your Spyder.
import turtle, random, time

score = 0

class RunawayGame:
    def __init__(self, canvas, runner, chaser, catch_radius=20, init_dist=400):
        self.canvas = canvas
        self.runner = runner
        self.chaser = chaser
        self.catch_radius2 = catch_radius**2

        # Initialize 'runner' and 'chaser'
        self.runner.shape('turtle')
        self.runner.color('blue')
        self.runner.penup()
        self.runner.setx(-init_dist / 2)

        self.chaser.shape('turtle')
        self.chaser.color('red')
        self.chaser.penup()
        self.chaser.setx(+init_dist / 2)
        self.chaser.setheading(180)

        # Instantiate an another turtle for drawing
        self.drawer = turtle.RawTurtle(canvas)
        self.drawer.setx(0)
        self.drawer.sety(0)
        self.drawer.hideturtle()
        self.drawer.penup()

    def is_catch(self):
        p = self.runner.pos()
        q = self.chaser.pos()
        dx, dy = p[0] - q[0], p[1] - q[1]
        return dx**2 + dy**2 < self.catch_radius2

    def start(self, ai_timer_msec=100):
        self.ai_timer_msec = ai_timer_msec
        self.start_time = time.time()
        self.canvas.ontimer(self.step, self.ai_timer_msec)

    def step(self):
        self.runner.run_ai(self.chaser)
        self.chaser.run_ai(self.runner)

        if (self.runner.pos()[0] < -320):
            self.runner.setx(320)
        if (self.runner.pos()[0] > 320):
            self.runner.setx(-320)
        if (self.runner.pos()[1] < -280):
            self.runner.sety(280)
        if (self.runner.pos()[1] > 280):
            self.runner.sety(-280)

        if (self.chaser.pos()[0] < -320):
            self.chaser.setx(320)
        if (self.chaser.pos()[0] > 320):
            self.chaser.setx(-320)
        if (self.chaser.pos()[1] < -280):
            self.chaser.sety(280)
        if (self.chaser.pos()[1] > 280):
            self.chaser.sety(-280)
        
        is_catched = self.is_catch()
        global score

        self.drawer.undo()
        self.drawer.penup()
        # self.drawer.setpos(-300, 300)
        elapse = time.time() - self.start_time
        self.drawer.write(f'Is catched? {is_catched} / Elapse: {elapse:.0f} / Score: {score}')

        if (is_catched == True):
            score += 1
            self.runner.setx(-200)
            self.runner.sety(0)
            self.chaser.setx(200)
            self.chaser.sety(0)

        self.canvas.ontimer(self.step, self.ai_timer_msec)

class ManualMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

        # Register event handlers
        canvas.onkeypress(lambda: self.forward(self.step_move), 'Up')
        canvas.onkeypress(lambda: self.backward(self.step_move), 'Down')
        canvas.onkeypress(lambda: self.left(self.step_turn), 'Left')
        canvas.onkeypress(lambda: self.right(self.step_turn), 'Right')
        canvas.listen()

    def run_ai(self, opponent):
        pass

class LessRandomMover(turtle.RawTurtle):
    def __init__(self, canvas, step_move=10, step_turn=10):
        super().__init__(canvas)
        self.step_move = step_move
        self.step_turn = step_turn

    def run_ai(self, oppoenent):
        opp_pos = oppoenent.pos()
        self_pos = self.pos()
        opp_x, opp_y = opp_pos[0], opp_pos[1]
        self_x, self_y = self_pos[0], self_pos[1]
        opp_heading = oppoenent.heading()
        mode = random.random()
        if mode < 0.6:
            self.forward(self.step_move)
        elif mode < 0.75:
            self.left(self.step_turn)
        elif mode < 0.9:
            self.right(self.step_turn)
        elif ((opp_x - self_x)**2 + (opp_y - self_y)**2) < 200**2:
            self.setheading(opp_heading)
        else:
            self.circle(30)


if __name__ == '__main__':
    canvas = turtle.Screen()
    runner = LessRandomMover(canvas)
    chaser = ManualMover(canvas)

    game = RunawayGame(canvas, runner, chaser)
    game.start()
    canvas.mainloop()