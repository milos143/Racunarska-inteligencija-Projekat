/* Naivna, rekurzivna implementacija problema maksimalnog ranca */
#include <stdio.h> 
#include <time.h>

//Deklaracije koriscenih funkcija
int max(int a, int b);


int main() { 
    clock_t pocetak, kraj;
    double cpu_time_used;

    int vrednosti[] = {45, 67, 69, 75}; 
					   
    int tezine[] = {9, 11, 10, 12}; 
    int  K = 20; 
    int n = sizeof(vrednosti)/sizeof(vrednosti[0]); 

    pocetak = clock(); 
    int t = ranac(K, tezine, vrednosti, n);
    kraj = clock();

	cpu_time_used = ((double)(kraj - pocetak))/CLOCKS_PER_SEC;

    printf("Rezultat: %d\n", t);
    printf("Vreme izvrsavanja: %lf\n", cpu_time_used); 

    return 0; 
} 

//Definicije koriscenih funkcija:

// Pomocna funkcija koja vraca maksimum svojih argumenata
int max(int a, int b){
	return (a > b)? a : b;
} 

// Funkcija vraca maksimalnu vrednost koja moze biti smestena u ranac kapaciteta K
int ranac(int K, int tezine[], int vrednosti[], int n){
   // Bazni slucaj
   if (n == 0 || K == 0) 
       return 0; 

   // Ako je tezina n-tog predmeta veca od kapaciteta ranca K
   // tada predmet nece biti ubacen u ranac.
   if (tezine[n-1] > K) 
       return ranac(K, tezine, vrednosti, n-1); 

   //Inace vraca maksimum naredna dva slucaja:
   //1. uzima se n-ti predmet 
   //2. ne uzima se n-ti predmet
   else return max( vrednosti[n-1] + ranac(K-tezine[n-1], tezine, vrednosti, n-1), 
                    ranac(K, tezine, vrednosti, n-1) 
                  ); 
} 