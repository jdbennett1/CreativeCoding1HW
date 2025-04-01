function setup() {
    createCanvas(400, 400);
  }
  
  function draw() {
    background(220);
    ellipse(95,168,75,67.5);
    ellipse(245,168,75,67.5);
    square(95,135,75);
    square(170,135,75);
    circle(170,285,75);
    square(132.5,210,75);

    line(95,210,132.5,285);
    line(245,210,207.5,285);

    triangle(143,135,170,75,197,135);
    circle(170,60,60);
    circle(200,75,18);
    circle(140,75,18);
    square(140,60,60);

    point(203,75);
    point(138,75);
    circle(155,75,12);
    circle(185,75,12);
    point(185,75);
    point(155,75);

  
    text("Yo!", 50,80);
    textSize(22);
    text("JD Bennett",130,360 );
    }
