# include <iostream>
# include <cmath>

using namespace std;

double factorial(double num){
   double x, h, res;
   x = 0;
   h = 0.000001;
   res = 0;
   while (x <= 40){
      res = res + h*exp(-x)*pow(x, num);
      x = x + h;
   }
   return res;
}

int main(){
   double y, a, b;
   int iter;
   iter = 0;
   cout << "Masukkan nilai faktorial yang ingin dicari : ";
   cin >> y;
   a = 0;
   b = 0;
   while (factorial(b) < y){
      b++;
   }
   a = b-1;
   while (iter <= 10){
      if (factorial((a+b)/2) < y){
         a = (a+b)/2;
      }
      else {
         b = (a+b)/2;
      iter++;
      }
   }
   cout << (a+b)/2;
   return 0;
}