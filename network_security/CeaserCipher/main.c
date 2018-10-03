#include <stdio.h>
#include <string.h>
//Ceaser cipher

void encrypt(char [], int);
void decrypt(char [], int);

int main(){
 int key,opt;
 char input[50];

 printf("Enter 1 to encrypt\nEnter 2 to decrypt\n");
 scanf("%d", &opt);


 switch(opt){
  case 1:
  getchar();
  printf("Enter plain text to encrypt:\n");
  scanf("%[^\n]s", &input);
  getchar();
  printf("Enter key:\n");
  scanf("%d", &key);

  encrypt(input, key);

  break;
  case 2:

  getchar();
  printf("Enter plain text to encrypt:\n");
  scanf("%[^\n]s", &input);
  getchar();
  printf("Enter key:\n");
  scanf("%d", &key);

  decrypt(input, key);

  break;

  default:

  break;
 }
 return 0;
}

void encrypt(char pt[50], int key){

  int val,i,size = strlen(pt);
  char ct[size];

  for(i=0;i<size;i++){
   val = pt[i]+key;
   if(pt[i]>=97&&pt[i]<=122){
     if(val>122)val-=26;
   }else if(pt[i]>=65&&pt[i]<=90){
    if(val>90)val-=26;
   }else val=pt[i];
   ct[i]=val;
  }
  printf("%s", ct);
}

void decrypt(char ct[50], int key){

  int val,i,size = strlen(ct);
  char pt[size];

  for(i=0;i<size;i++){
   val = ct[i]-key;
   if(ct[i]>=97&&ct[i]<=122){
     if(val<97)val+=26;
   }else if(ct[i]>=65&&ct[i]<=90){
    if(val<65)val+=26;
   }else val=ct[i];
   pt[i]=val;
  }
  printf("%s", pt);
}
