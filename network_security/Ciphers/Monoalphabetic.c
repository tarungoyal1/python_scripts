#include <stdio.h>
#include <string.h>
char alpha[26] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};

void encrypt(char[], char[]);

void decrypt(char[], char[]);

int main(){

int opt;
char pt[50], key[26], ct[50];

    printf("Enter 1 to encrypt\nEnter 2 to decrpyt\n");
    scanf("%d", &opt);

    switch(opt){
     case 1:
      getchar();
      printf("Enter plaintext:");
      scanf("%[a-z ]", &pt);
      printf("Plaintext: %s\n", pt);
      getchar();
      printf("Enter unique key of 26 chars:");
      scanf("%[a-z]",  &key);
      encrypt(pt, key);
     break;
     case 2:
       getchar();
       printfs
       d("Enter cipher text:");
       scanf("%[a-z ]", &ct);
       printf("Cipher text: %s\n", ct);
       getchar();
       printf("Enter unique key of 26 chars:");
       scanf("%[a-z]", &key);
      decrypt(ct, key);
     break;
    }

    return 0;
}

void encrypt(char pt[], char key[]){
    char ct[50];
    printf("%s\n",alpha);
    for(int i=0;i<26;i++)printf("|");
    printf("\n%s\n", key);

    for(int i=0;i<strlen(pt);i++){
     if(pt[i]<97||pt[i]>122){
      ct[i]=pt[i];
      continue;
     }
        for(int j=0;j<26;j++){
          if(pt[i]==alpha[j]){
            ct[i]=key[j];
            break;
          }
        }
    }
    printf("Cipher text:\n");
    printf("%s", ct);
}

void decrypt(char ct[], char key[]){
    char pt[50];
    printf("%s\n",key);
    for(int i=0;i<26;i++)printf("|");
    printf("\n%s\n", alpha);

    for(int i=0;i<strlen(ct);i++){
     if(ct[i]<97||ct[i]>122){
      pt[i]=ct[i];
      continue;
     }
        for(int j=0;j<26;j++){
          if(ct[i]==key[j]){
            pt[i]=alpha[j];
            break;
          }
        }
    }
    printf("Plain text:\n");
    printf("%s", pt);
}
