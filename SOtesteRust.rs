use std::io;

fn main() {
    println!("Digite o nome:");
    
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("Erro ao ler a entrada");
    
    let name = input.trim();
    
    if name == "Lenz" || name == "lenz" || name == "LENZ" {
        println!("Bem-vindo, Lenz!");
    } else {
        println!("Impostor!");
    }
}