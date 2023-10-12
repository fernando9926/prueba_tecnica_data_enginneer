import scala.util.Random

class ConjuntoNumeros {
  private val conjunto: Set[Int] = (1 to 100).toSet
  private var numeroExtraccion: Option[Int] = None

  def extraerNumero(numeroDeseado: Int): Boolean = {
    if (numeroDeseado >= 1 && numeroDeseado <= 100 && conjunto.contains(numeroDeseado)) {
      numeroExtraccion = Some(numeroDeseado)
      true
    } else {
      false
    }
  }

  def obtenerNumeroExtraccion: Option[Int] = numeroExtraccion
}

object Main {
  def main(args: Array[String]): Unit = {
    val input = scala.io.StdIn.readLine()
    try {
      val numeroDeseado = input.toInt
      val conjuntoNumeros = new ConjuntoNumeros()

      if (conjuntoNumeros.extraerNumero(numeroDeseado)) {
        println(s"Se extrajo el número $numeroDeseado.")
      } else {
        println("El número no es válido o ya ha sido extraído previamente.")
      }
    } catch {
      case e: NumberFormatException =>
        println("Por favor, ingrese un número válido.")
    }
  }
}