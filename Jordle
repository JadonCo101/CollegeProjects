import java.util.ArrayList;
import java.util.Arrays;
import javafx.stage.WindowEvent;
import javafx.application.Application;
import javafx.geometry.Pos;
import java.util.Random;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.shape.Rectangle;
import javafx.scene.control.Label;
import javafx.scene.layout.GridPane;
import javafx.geometry.Insets;
import javafx.scene.layout.BorderPane;
import javafx.scene.control.Alert;
import javafx.scene.control.Alert.AlertType;
import javafx.scene.layout.HBox;
import javafx.scene.paint.Color;
import javafx.stage.Stage;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.Pane;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.scene.text.TextAlignment;
import javafx.scene.layout.Priority;
import javafx.event.EventHandler;
import javafx.event.ActionEvent;
import javafx.scene.input.KeyEvent;


/**
 * main Jordle class.
 */
public class Jordle extends Application {
    private static String bgColor = "white";
    private static String buttonColor = "000000";
    private static Color tileColor = Color.GREY;
    private static int letters = 5;
    private static int guesses = 6;
    private static Color displayColor = Color.BLACK;
    private static int wordCount = 0;
    private static int count = 0;
    private static int level = 0;
    private String word;
    private String leaderBoardString = "";

    /**
     * @param args -main method that runs the Jordle Program
     */
    public static void main(String[] args) {
        launch(args);
    }

    /**
     * @param primaryStage - creates the main window for the Jordle program
     */
    @Override
    public void start(Stage primaryStage) {
        while (level == 0) {
            Random rand = new Random();
            word = Words.list.get((rand.nextInt((28) + 1)));
            level += 1;
        } //choose the word for the jordle game
        //border pane, scene, and main stage
        BorderPane pane = new BorderPane();
        pane.setStyle("-fx-background-color: " + bgColor);
        Scene scene = new Scene(pane, 700, 750);
        primaryStage.setScene(scene);
        primaryStage.setTitle("Jordle"); // Set the stage title
        primaryStage.show(); // Display the primary stage

        //title hbox - "Jordle"
        HBox hbox = new HBox();
        hbox.setSpacing(10);
        Text title = new Text("Jordle");
        title.setFont(Font.font("Times New Roman", FontWeight.BLACK, FontPosture.ITALIC, 50.0));
        title.setFill(Color.GREEN);
        title.setTextAlignment(TextAlignment.CENTER);
        hbox.getChildren().addAll(title);
        hbox.setAlignment(Pos.CENTER);

        //words - default
        Text display = new Text("Try guessing a word!");
        display.setFont(Font.font("Times New Roman", 30.0));
        display.setTextAlignment(TextAlignment.CENTER);
        display.setFont(Font.font("Times New Roman", 30.0));
        if (bgColor.equals("white")) {
            display.setFill(Color.BLACK);
        } else if (bgColor.equals("black")) {
            display.setFill(Color.WHITE);
        }


        //Light & dark mode change
        Button mode = new Button("      Change to \nLight/Dark Mode");
        mode.setStyle("-fx-background-color: grey;" + "-fx-text-fill: #" + buttonColor + ";");
        mode.setAlignment(Pos.CENTER);
        mode.setFocusTraversable(false);
        mode.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                changeBackground();
                pane.setStyle("-fx-background-color: " + bgColor);
                display.setFill(displayColor);
            }
        });

        //instruction button
        Button instruct = new Button("Instructions");
        Font instructFont = Font.font("Verdana", FontWeight.MEDIUM, 15);
        instruct.setFont(instructFont);
        instruct.setStyle("-fx-text-fill: #000000;" + "-fx-background-color: #6A8CFF;");
        instruct.resize(primaryStage.getWidth() / 4, primaryStage.getHeight() / 4);
        instruct.setPadding(new Insets(20, 20, 20, 20));
        instruct.setFocusTraversable(false);
        instruct.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Alert instruct = new Alert(AlertType.INFORMATION, "Jordle - "
                        + "A fairly simple game that requires the user to guess the "
                        + letters + " letter word in " + guesses + " or less tries. The guesses "
                        + "must be " + letters + "-letter words and CANNOT be less than said number. "
                        + "Green Boxes mean that character is in the correct spot and Yellow Boxes "
                        + "mean that the character is somewhere in the word but not in the "
                        + "same spot. Good luck and have fun :) \n\n Developed by Jadon Co");
                instruct.setHeaderText("Instructions");
                instruct.show();
            }
        });
        //gridpane wordle
        GridPane main = new GridPane();
        Tile[][] jordleBoard = new Tile[6][5];
        main.setPrefWidth(500);
        main.setPrefHeight(700);
        main.setHgap(10);
        main.setVgap(10);
        Font jordleChar = Font.font("Times New Roman", FontWeight.BOLD, FontPosture.REGULAR, 40);
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 5; j++) {
                jordleBoard[i][j] = new Tile("", Color.LIGHTSLATEGRAY, jordleChar);
            }
        }
        for (int i = 0; i < 6; i++) {
            for (int j = 0; j < 5; j++) {
                main.add(jordleBoard[i][j], j, i);
                Label lab = new Label((jordleBoard[i][j]).getChar());
                lab.setFont((jordleBoard[i][j]).getFont());
                lab.setTextFill(Color.WHITE);
                (jordleBoard[i][j]).getChildren().addAll(new Rectangle(100, 75, (jordleBoard[i][j]).getColor()), lab);
            }
        }
        main.setAlignment(Pos.CENTER);
        scene.setOnKeyPressed(new EventHandler<KeyEvent>() {
            @Override
            public void handle(KeyEvent event) {
                if ((event.getCode()).isLetterKey()) {
                    if (count <= 4) {
                        (jordleBoard[wordCount][count]).setChar(event.getText());
                        main.getChildren().remove(jordleBoard[wordCount][count]);
                        (jordleBoard[wordCount][count]).setChar(event.getText());
                        Label lab = new Label((jordleBoard[wordCount][count]).getChar());
                        lab.setFont((jordleBoard[wordCount][count]).getFont());
                        lab.setStyle("-fx-text-fill: #0400D7;");
                        (jordleBoard[wordCount][count]).getChildren().addAll(new Rectangle(100, 75,
                                        (jordleBoard[wordCount][count]).getColor()),
                                lab);
                        main.add(jordleBoard[wordCount][count], count, wordCount);
                        count += 1;
                    }
                } else if (event.getCode().getName().equals("Enter")) {
                    if (count >= 5 && wordCount <= 5) {
                        String answer = "";
                        for (int i = 0; i < 5; i++) {
                            if (word.contains(jordleBoard[wordCount][i].getChar())
                                    && (!answer.contains(event.getCode().getName()))) {
                                if ((word.indexOf((jordleBoard[wordCount][i].getChar())) == i)) {
                                    jordleBoard[wordCount][i].setColor(Color.GREEN);
                                    main.getChildren().remove(jordleBoard[wordCount][i]);
                                    Label lab = new Label((jordleBoard[wordCount][i]).getChar());
                                    lab.setFont((jordleBoard[wordCount][i]).getFont());
                                    lab.setStyle("-fx-text-fill: #0400D7;");
                                    Rectangle tangle = new Rectangle(100, 75,
                                            (jordleBoard[wordCount][i]).getColor());
                                    (jordleBoard[wordCount][i]).getChildren().addAll(tangle, lab);


                                    main.add(jordleBoard[wordCount][i], i, wordCount);
                                } else {
                                    jordleBoard[wordCount][i].setColor(Color.YELLOW);
                                    main.getChildren().remove(jordleBoard[wordCount][i]);
                                    Label lab = new Label((jordleBoard[wordCount][i]).getChar());
                                    lab.setFont((jordleBoard[wordCount][i]).getFont());
                                    lab.setStyle("-fx-text-fill: #0400D7;");
                                    Rectangle tangle = new Rectangle(100, 75,
                                            (jordleBoard[wordCount][i]).getColor());
                                    (jordleBoard[wordCount][i]).getChildren().addAll(tangle, lab);
                                    main.add(jordleBoard[wordCount][i], i, wordCount);
                                }
                            } else {
                                jordleBoard[wordCount][i].setColor(Color.DARKGRAY);
                                main.getChildren().remove(jordleBoard[wordCount][i]);
                                Label lab = new Label((jordleBoard[wordCount][i]).getChar());
                                lab.setFont((jordleBoard[wordCount][i]).getFont());
                                lab.setStyle("-fx-text-fill: #0400D7;");
                                Rectangle tangle = new Rectangle(100, 75,
                                        (jordleBoard[wordCount][i]).getColor());
                                (jordleBoard[wordCount][i]).getChildren().addAll(tangle, lab);
                                main.add(jordleBoard[wordCount][i], i, wordCount);
                            }
                            answer += jordleBoard[wordCount][i].getChar();
                        }
                        if (word.equals(answer)) {
                            display.setText("You have correctly\n guessed the word!");
                            display.setTextAlignment(TextAlignment.CENTER);
                            Alert win = new Alert(AlertType.INFORMATION, "Congrats, you guessed the "
                                    + "correct word (" + word + ") in " + (wordCount + 1) + " tries!!!");
                            win.setHeaderText("Winner Winner, Chicken Dinner");
                            win.show();
                            win.setOnCloseRequest(close -> {
                                restart(primaryStage);
                                leaderBoardString += "\n" + word + ": " + (wordCount) + " tries";
                                Random randthing = new Random();
                                word = Words.list.get((randthing.nextInt((28) + 1)));
                                count = 0;
                                wordCount = 0;
                            });
                        } else if (wordCount == 5) {
                            display.setText("You have lost :(");
                            display.setTextAlignment(TextAlignment.CENTER);
                            Alert lose = new Alert(AlertType.INFORMATION, "Unfortunately, you have used "
                                    + "6 guesses and have not guessed the correct word, which was: " + word + ". "
                                    + "Try again you got it :)");
                            lose.setHeaderText("You Lost :(");
                            lose.show();
                            lose.setOnCloseRequest(close -> {
                                restart(primaryStage);
                                leaderBoardString += "\n" + word + ": +6 tries";
                                Random randthing = new Random();
                                word = Words.list.get((randthing.nextInt((28) + 1)));
                                count = 0;
                                wordCount = 0;
                            });
                        }
                        count = 0;
                        wordCount += 1;
                    } else {
                        Alert lessThan = new Alert(AlertType.INFORMATION, "bro you need to type 5 letters"
                                + " before pressing enter, you are trolling");
                        lessThan.setHeaderText("Error Message");
                        jordleBoard[wordCount][count].requestFocus();
                        lessThan.show();
                    }
                } else if (event.getCode().getName().equals("Backspace") && count > 0) {
                    count -= 1;
                    main.getChildren().remove(jordleBoard[wordCount][count]);
                    (jordleBoard[wordCount][count]).setChar("");
                    Label lab = new Label((jordleBoard[wordCount][count]).getChar());
                    lab.setFont((jordleBoard[wordCount][count]).getFont());
                    lab.setStyle("-fx-text-fill: #0400D7;");
                    (jordleBoard[wordCount][count]).getChildren().addAll(new Rectangle(100, 75,
                            (jordleBoard[wordCount][count]).getColor()), lab);
                    main.add(jordleBoard[wordCount][count], count, wordCount);
                }
            }

        });
        //restart the entire jordle game
        Button restart = new Button("Restart");
        Font font = Font.font("Verdana", FontWeight.MEDIUM, 15);
        restart.setFont(font);
        restart.resize(20, 20);
        restart.setStyle("-fx-text-fill: #000000;" + "-fx-background-color: #FF9C2D;");
        restart.setPadding(new Insets(20, 20, 20, 20));
        restart.setFocusTraversable(false);
        restart.setOnAction(actionEvent ->  {
            restart(primaryStage);
            Random randthing = new Random();
            word = Words.list.get((randthing.nextInt((28) + 1)));
            count = 0;
            wordCount = 0;
        });
        //bot HBox for words, restart button, and instruction
        HBox botBox = new HBox();
        botBox.setPadding(new Insets(20, 20, 20, 20));
        Pane spacingThing = new Pane();
        Pane leftbotside = new Pane();
        leftbotside.setPrefSize(10, 10);
        botBox.setHgrow(spacingThing, Priority.ALWAYS);
        botBox.getChildren().addAll(leftbotside, display, spacingThing, restart, instruct);
        botBox.setPadding(new Insets(20, 15, 20, 20));
        botBox.setSpacing(20.0);
        //Leaderboard
        Button board = new Button("Leaderboard");
        board.setStyle("-fx-background-color: grey;" + "-fx-text-fill: #" + buttonColor + ";");
        board.setAlignment(Pos.CENTER);
        HBox boardBox = new HBox();
        boardBox.getChildren().addAll(mode);
        boardBox.setAlignment(Pos.CENTER);
        boardBox.setPadding(new Insets(30, 30, 20, 20));
        board.setFocusTraversable(false);
        board.setOnAction(new EventHandler<ActionEvent>() {
            public void handle(ActionEvent event) {
                Alert leader = new Alert(AlertType.INFORMATION, "This is the leaderboard: "
                        + leaderBoardString);
                leader.setHeaderText("LeaderBoard");
                leader.show();
            }
        });
        //Borderpane configuration
        Pane spacer = new Pane();
        spacer.setPrefSize(50, 50);
        HBox temp = new HBox();
        temp.setHgrow(hbox, Priority.ALWAYS);
        temp.setHgrow(mode, Priority.ALWAYS);
        temp.getChildren().addAll(board, hbox, mode);
        temp.setPadding(new Insets(20, 30, 10, 30));
        pane.setBottom(botBox);
        pane.setTop(temp);
        pane.setCenter(main);
        pane.setPadding(new Insets(20, 30, 10, 30));
        primaryStage.setTitle("Jordle"); // Set the stage title
        primaryStage.show(); // Display the primary stage
        primaryStage.setOnCloseRequest(new EventHandler<WindowEvent>() {
            @Override
            public void handle(WindowEvent e) {
                leaderBoardString = "";
            }
        });
    }

    /**
     * Changes the background from light to dark mode (including text).
     */
    public void changeBackground() {
        if (bgColor.equals("black")) {
            bgColor = "white";
            displayColor = Color.BLACK;
            tileColor = Color.LIGHTSLATEGRAY;
            buttonColor = "000000";
        } else if (bgColor.equals("white")) {
            bgColor = "black";
            displayColor = Color.WHITE;
            tileColor = Color.LIGHTSLATEGRAY;
            buttonColor = "FFFFFF";
        }
    }

    /**
     * @param stage - passes pimary stage into method and completely restarts the window
     */
    public void restart(Stage stage) {
        start(stage);
    }

}

/**
 * class that used to extend StackPane and create a custom pane that is used for the boxes in the Jordle Game.
 */
class Tile extends StackPane {
    private String character;
    private Color color;
    private Font font;

    Tile(String character, Color color, Font font) {
        this.character = character;
        this.color = color;
        this.font = font;
    }

    public Color getColor() {
        return this.color;
    }
    public String getChar() {
        return this.character;
    }
    public Font getFont() {
        return this.font;
    }


    public void setColor(Color color) {
        this.color = color;
    }
    public void setChar(String characterThingy) {
        this.character = characterThingy;
    }



}


/**
 * List of words for the Jordle Game.
 */
class Words {
    public static ArrayList<String> list = new ArrayList<>(Arrays.asList(
            "alert", "bound", "break", "clear", "close", "codes", "enums", "false", "files", "final", "float", "index",
            "inset", "logic", "mouse", "nodes", "pixel", "print", "scope", "short", "stack", "stage", "super", "throw",
            "token", "value", "while", "world", "write"
    ));

    // use this ArrayList if you want to attempt one of the extra credit options (accounting for duplicate characters)
    /**
     public static ArrayList<String> list = new ArrayList<>(Arrays.asList(
     "array", "catch", "class","error", "event", "hello", "inner", "javac", "merge", "nlogn", "queue", "scene"
     ));
     */

}




//javac --module-path javafx-sdk-11.0.2/lib --add-modules javafx.controls Jordle.java
//java --module-path javafx-sdk-11.0.2/lib --add-modules javafx.controls Jordle


