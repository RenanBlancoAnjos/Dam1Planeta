import java.util.Scanner;

public class Concatenar {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduce un nombre");
        String nombre = scanner.nextLine();

        System.out.println("Bienvenido " + nombre);

        scanner.close();
    }
}
