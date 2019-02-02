//Problem ranca resen dinamickim programiranjem
#include <stdio.h> 
#include <time.h> 
  
/*Deklaracije koriscenih funkcija*/
int max(int a, int b);
int ranac(int kapacitet, int tezine[], int vrednosti[], int n);
  
int main(){ 
    clock_t pocetak, kraj;
    double cpu_time_used;

    int vrednosti[] = {45, 67, 69, 75}; 
    int tezine[] = {9, 11, 10, 12}; 
    int  kapacitet = 20; 
    int n = sizeof(vrednosti)/sizeof(vrednosti[0]); 
    
    pocetak = clock();
    int t = ranac(kapacitet, tezine, vrednosti, n);
    kraj = clock();

    cpu_time_used = ((double)(kraj - pocetak))/CLOCKS_PER_SEC;

    printf("%d\n", t);
    printf("Vreme izvrsavanja: %lf\n", cpu_time_used);
    return 0; 
} 
/*Definicije koriscenih funkcija*/

//Pomocna funkcija koja vraca maksimum svojih argumenata
int max(int a, int b){ 
  return (a > b)? a : b; 
} 

//Funkcija vraca maksimalnu vrednost koja moze biti smestena u ranac kapaciteta K
int ranac(int kapacitet, int tezine[], int vrednosti[], int n){ 

   int K[n+1][kapacitet+1]; 
  
   //Popunjavanje tabele odozdo nagore
   for (int i = 0; i <= n; i++){ 
       for (int w = 0; w <= kapacitet; w++){ 
           if (i==0 || w==0) 
               K[i][w] = 0; 
           else if (tezine[i-1] <= w) 
                 K[i][w] = max(vrednosti[i-1] + K[i-1][w-tezine[i-1]],  K[i-1][w]); 
           else
                 K[i][w] = K[i-1][w]; 
       } 
   } 
   return K[n][kapacitet]; 
}
