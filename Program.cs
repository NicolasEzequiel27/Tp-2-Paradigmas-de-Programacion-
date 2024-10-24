using System;
using System.Collections.Generic;

public class Alumno
{
    public string Nombre { get; set; }
    public List<float> Notas { get; set; }

    public Alumno(string nombre)
    {
        Nombre = nombre;
        Notas = new List<float>();
    }

    public float Promedio()
    {
        if (Notas.Count == 0) return 0;
        float suma = 0;
        foreach (var nota in Notas)
        {
            suma += nota;
        }
        return suma / Notas.Count;
    }

    // Método que retorna el estado del alumno basado en el promedio
    public string ObtenerEstado()
    {
        float promedio = Promedio();
        
        if (promedio >= 1 && promedio < 6)
        {
            return "DEBE RECURSAR LA MATERIA";
        }
        else if (promedio >= 6 && promedio <= 7.5)
        {
            return "REGULAR";
        }
        else if (promedio >= 7.5 && promedio < 8)
        {
            return "POSIBLE PROMOCION";
        }
        else if (promedio >= 8 && promedio <= 10)
        {
            return "PROMOCIONADO";
        }
        else
        {
            return "SIN CALIFICACIÓN";
        }
    }
}

class Program
{
    static List<Alumno> listaAlumnos = new List<Alumno>();

    static void Main(string[] args)
    {
        int opcion;
        do
        {
            Console.Clear();
            Console.WriteLine("Gestión de Alumnos - Paradigmas de Programación");
            Console.WriteLine("1. Ingresar Alumno y Notas");
            Console.WriteLine("2. Ver Listado de Alumnos, Promedios y Estado");
            Console.WriteLine("3. Salir");
            Console.Write("Seleccione una opción: ");
            
            if (!int.TryParse(Console.ReadLine(), out opcion))
            {
                Console.WriteLine("Por favor ingrese un número válido.");
                continue;
            }

            switch (opcion)
            {
                case 1:
                    IngresarAlumno();
                    break;
                case 2:
                    VerListadoAlumnos();
                    break;
            }
        } while (opcion != 3);
    }

    static void IngresarAlumno()
    {
        Console.Clear();
        Console.WriteLine("Ingrese el nombre del alumno:");
        string nombre = Console.ReadLine();
        var alumno = new Alumno(nombre);

        Console.WriteLine("Ingrese las notas del alumno (ingrese -1 para finalizar):");
        float nota;
        do
        {
            Console.Write("Nota: ");
            
            if (!float.TryParse(Console.ReadLine(), out nota))
            {
                Console.WriteLine("Por favor, ingrese un número válido.");
                continue;
            }

            if (nota != -1)
            {
                alumno.Notas.Add(nota);
            }

        } while (nota != -1);

        listaAlumnos.Add(alumno);

        Console.WriteLine("Alumno y notas ingresados correctamente.");
        Console.ReadLine();
    }

    static void VerListadoAlumnos()
    {
        Console.Clear();
        Console.WriteLine("Listado de Alumnos, Promedios y Estado:");

        if (listaAlumnos.Count == 0)
        {
            Console.WriteLine("No hay alumnos ingresados.");
        }
        else
        {
            foreach (var alumno in listaAlumnos)
            {
                Console.WriteLine($"Alumno: {alumno.Nombre} - Promedio: {alumno.Promedio():0.00} - Estado: {alumno.ObtenerEstado()}");
            }
        }

        Console.ReadLine();
    }
}
