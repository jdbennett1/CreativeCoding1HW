function setup() {
  new Canvas(windowWidth, windowHeight);
  ball = new Sprite();

  textSize(24);
  textAlign(CENTER, CENTER);
  fill(255);

  canvas.mousePressed(() => {
    canvas.canvas.focus();
  });
}

function draw() {
  background('black');

  if (!focused) {
    text('Click to activate controls', width / 2, height / 2);
    return;
  }

  ball.vel.x = 0;
  ball.vel.y = 0;

  if (kb.pressing('left')) {
    ball.vel.x = -5;
  }
  if (kb.pressing('right')) {
    ball.vel.x = 5;
  }
  if (kb.pressing('up')) {
    ball.vel.y = -5;
  }
  if (kb.pressing('down')) {
    ball.vel.y = 5;
  }

  drawSprites();
}