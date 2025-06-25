//we are making a game in which the comp is going to select a random number between 1-100 and the user is going to guess that number and we are going the user to guess until the user guesses the number or entered stop
import java.util.Scanner;
public class project_in_java {
    public static void main(String[] args) {
        Scanner guess = new Scanner(System.in);
        int myNum = (int) (Math.random()*100);
        int userGuess;
do {
    System.out.println("enter your guess number(1-100) :");
    userGuess= guess.nextInt();
    if (userGuess == myNum) {
        System.out.println("CORRECT GUESS!!!");
        break;
    }
    else if(userGuess > myNum){
        System.out.println("your guessed number is larger than the actual number");
    }
    else{
        System.out.println("your guessed number is smaller than the actual number");
    }
    }   while(userGuess >=0);
        System.out.println("my guessed number is :");
        System.out.println(userGuess);
    }
}
