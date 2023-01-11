// Demonstrate primitve drawing in SFML
#include<iostream>
using namespace std;


#include "SFML/Graphics.hpp"

int main() {

    //game set up (you'll need these two lines in every game)
    sf::RenderWindow renderWindow(sf::VideoMode(500, 500), "Pong Paddle"); //set up screen
    sf::Event event; //set up event queue

    //paddle1 set up
    sf::RectangleShape paddle1(sf::Vector2f(20.0f, 100.0f));
    paddle1.setFillColor(sf::Color::Blue); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    paddle1.setPosition(30.0f, 250.0f); //set position: this is where the top left corner will be

    //paddle2 set up
    sf::RectangleShape paddle2(sf::Vector2f(20.0f, 100.0f));
    paddle2.setFillColor(sf::Color::Blue); //other colors: https://www.sfml-dev.org/documentation/2.5.1/classsf_1_1Color.php
    paddle2.setPosition(450.0f, 250.0f); //set position: this is where the top left corner will be
    
    //ball set up
    float ballX = 250;
    float ballY = 250;
    float xVel = 10;
    float yVel =10;
    sf::CircleShape ball(20); //sets radius of circle
    ball.setFillColor(sf::Color(200, 50, 50)); //numbers and color names
    ball.setPosition(ballX, ballY); //position

    


    //################### HOLD ONTO YOUR BUTTS, ITS THE GAME LOOP###############################################################
    while (renderWindow.isOpen()) {//keep window open until user shuts it down
        while (renderWindow.pollEvent(event)) { //look for events

            //this checks if the user has clicked the little "x" button in the top right corner
            if (event.type == sf::Event::EventType::Closed)
                renderWindow.close();

            //KEYBOARD INPUT (just one key to start
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::W)) { //checks if "W" is pressed
                paddle1.move(0, -5);
            } //move the rectangle 5 pixels UP on the y axis
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::S)) { //checks if "s" is pressed
                paddle1.move(0, 5); //move the rectangle 5 pixels UP on the y axis
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) { //checks if "up" is pressed
                paddle2.move(0, -5);
            } //move the rectangle 5 pixels UP on the y axis
            else if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) { //checks if "down" is pressed
                paddle2.move(0, 5); //move the rectangle 5 pixels UP on the y axis
            }
            //physics section

            if (ballX < 0 || ballX >400) {
                xVel *= -1;
            }

            ballX += xVel;
            ballY += yVel;

            ball.setPosition(ballX, ballY);
            
            //render section-----------------------------------------
            renderWindow.clear(); //wipes screen, without this things smear
            renderWindow.draw(paddle1); //you gotta drew each object
            renderWindow.draw(paddle2); //you gotta drew each object
            renderWindow.draw(ball);
            renderWindow.display(); //flips memory drawings onto screen
            
        }//######################## end game loop ###################################################################################


    }
    cout << "goodbye!" << endl;
} //end game
