import java.util.Scanner;

class Node {
    int id_no;
    int pin;
    String name;
    int cash;
    Node next;
    Node prev;

    Node() {
        this.id_no = 0;
        this.pin = 0;
        this.name = "";
        this.cash = 0;
        this.next = null;
        this.prev = null;
    }
}

class ATM {
    private Node head;
    private int y, z, c;
    private final Scanner scanner;

    ATM() {
        this.head = null;
        this.y = 0;
        this.z = 0;
        this.c = 0;
        this.scanner = new Scanner(System.in);
    }

    void CreateACC() {
        scanner.nextLine(); // Consume any leftover newline
        System.out.print("Enter Name: ");
        String name = scanner.nextLine();
        System.out.print("Enter ID No: ");
        int id_no = scanner.nextInt();
        System.out.print("Enter Pin: ");
        int pin = scanner.nextInt();
        
        Node newNode = new Node();
        newNode.name = name;
        newNode.id_no = id_no;
        newNode.pin = pin;
        newNode.cash = 0;
        
        if (head == null) {
            head = newNode;
        } else {
            Node temp = head;
            while (temp.next != null) {
                temp = temp.next;
            }
            temp.next = newNode;
            newNode.prev = temp;
        }
        System.out.println("Account Created Successfully");
    }

    void LOGIN_TO_ACCOUNT() {
        System.out.print("Enter ID No: ");
        y = scanner.nextInt();
        System.out.print("Enter Your PIN: ");
        z = scanner.nextInt();
        
        Node temp = head;
        while (temp != null) {
            if (temp.id_no == y && temp.pin == z) {
                System.out.println("Login Successful, Welcome " + temp.name);
                user_menu();
                return;
            }
            temp = temp.next;
        }
        System.out.println("Incorrect ID No or PIN");
    }

    void Deposit() {
        Node temp = head;
        while (temp != null) {
            if (temp.id_no == y && temp.pin == z) {
                System.out.print("Enter The Amount: ");
                c = scanner.nextInt();
                temp.cash += c;
                System.out.println("Amount successfully added");
                return;
            }
            temp = temp.next;
        }
    }

    void Balance_Enquiry() {
        Node temp = head;
        while (temp != null) {
            if (temp.id_no == y && temp.pin == z) {
                System.out.println("Name: " + temp.name);
                System.out.println("Your Balance is: " + temp.cash);
                return;
            }
            temp = temp.next;
        }
    }

    void Withdraw() {
        Node temp = head;
        while (temp != null) {
            if (temp.id_no == y && temp.pin == z) {
                System.out.print("Enter The Amount: ");
                c = scanner.nextInt();
                if (temp.cash >= c) {
                    temp.cash -= c;
                    System.out.println("Amount Successfully Withdrawn");
                } else {
                    System.out.println("Insufficient Balance");
                }
                return;
            }
            temp = temp.next;
        }
    }

    void user_menu() {
        while (true) {
            System.out.println("USER MENU");
            System.out.println("1. Deposit Money");
            System.out.println("2. Withdraw Money");
            System.out.println("3. Check Balance");
            System.out.println("4. Main Menu");
            System.out.print("Enter the Command: ");
            int command = scanner.nextInt();
            switch (command) {
                case 1 -> Deposit();
                case 2 -> Withdraw();
                case 3 -> Balance_Enquiry();
                case 4 -> {
                    main_menu();
                    return;
                }
                default -> System.out.println("Invalid Command, Try Again");
            }
        }
    }

    void main_menu() {
        while (true) {
            System.out.println("***********");
            System.out.println("MAIN MENU");
            System.out.println("1. Create Account");
            System.out.println("2. Login to Account");
            System.out.println("3. Exit");
            System.out.print("Enter the Command: ");
            int Scommand = scanner.nextInt();
            switch (Scommand) {
                case 1 -> CreateACC();
                case 2 -> LOGIN_TO_ACCOUNT();
                case 3 -> {
                    System.out.println("Thanks For Choosing TPC ATM");
                    System.out.println("***********");
                    System.exit(0);
                }
                default -> System.out.println("Invalid Command, Try Again");
            }
        }
    }

    public static void main(String[] args) {
        System.out.println("***********");
        System.out.println("WELCOME TO THE TPC ATM BANKING");
        System.out.println("***********");
        ATM obj = new ATM();
        obj.main_menu();
    }
}
