<h1> Python Project 6: Reeborg's Maze </h1>
<h2>Summary</h2>
<p>This project is for day 6 of the 100 Days of Code challenge that I'm completing as part of the Complete Python Pro Bootcamp with Dr. Angela Yu from the London App Brewery. Each project in this challenge will be using Python so that I can grow my skills in software development.</p>
<p>This project creates directions for Reeborg (a cartoon robot from <a href="https://reeborg.ca/reeborg.html" target="_blank">Reeborg's World</a>) to exit a maze. Reeborg has several functions predefined, such as turn_left() and front_is_clear(). In this project, I created a turn_right() function and used while loops and if/elif/else conditionals to program Reeborg to leave the maze. Each attempt/refresh will randomly assign Reeborg a location and facing-direction in the maze.</p>
<h3>Learnings</h3>
<p>I learned that keeping the robot to the edge along the wall (in this case the right side) helps to maintain consistency and structure when Reeborg could appear in any location and face any direction. I also learned that using "not" in front of a function can improve readability when learning to code. For example, "while not at_goal():" reads more easily than "while at_goal() != True:" </p>
<p>In while loops, I also found that it is easy to fall into an infinite loop if all reasonable conditions are not considered. As Reeborg is randomly placed in the maze, it needs a starting point. By adding the first while loop, it programs Reeborg to seek out a wall on its right so that it can follow along the right side of the maze until it reaches its goal. Without finding this starting point, Reeborg may end up continually turning in a 2x2 square formation, depending on where it is placed at each new maze attempt.</p>
<h2>Tech stack</h2>
<ul>
  <li>Python</li>
  <li><a href="https://reeborg.ca/reeborg.html" target="_blank">Reeborg's World</a></li>
</ul>
