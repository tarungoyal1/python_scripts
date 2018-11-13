#include<stdio.h>
#include<string.h>

int s=26,ptSize=0,keySize;
char alpha[26], key[20], pt[50], finalKey[50], ct[50];
int reftable[26][26];
int i,j,val,temp=-1,rowIndex=0,colIndex=0, opt;

void encrpyt();
void decrypt();
void printRefTable();

int main(){

//intializing alpha array
for(i=0;i<26;i++)alpha[i]=i+97;

//for(i=0;i<26;i++)printf("%c", alpha[i]);

for(i=0;i<s;i++){
 for(j=0;j<s;j++){
  if(i+j>s-1)
   reftable[i][j]=++temp;
  else
  reftable[i][j]=i+j;
 }
 temp=-1;
}
//kincmlhupf

printf("Enter key:");
scanf("%[a-z]", &key);
printf("Your key  = %s\n", key);
getchar();
printf("Enter text:");
scanf("%[a-z]", &pt);
printf("Your text = %s\n", pt);

ptSize=strlen(pt);
keySize=strlen(key);


//printf("Plain text size = %d\n",ptSize);
//printf("Key size = %d\n",keySize);

//preparing final key
j=0;
for(i=0;i<ptSize;i++){
 if(j>keySize-1) j=0;
 finalKey[i]=key[j];
 ++j;
}

printRefTable();

printf("Enter option:\n1 to encrypt\n2 to decrypt\n");
scanf("%d",&opt);

switch(opt){
 case 1:
  encrpyt();
 break;
 case 2:
  decrypt();
 break;
 default:
  printf("Enter valid option!");
 break;
}

 return 0;
}

void encrpyt(){
printf("%s\n",finalKey);
for(i=0;i<ptSize;i++)printf("|");
printf("\n");
printf("%s\n",pt);

for(i=0;i<ptSize;i++){

 rowIndex = finalKey[i]-97;
 colIndex = pt[i]-97;

 ct[i] = alpha[reftable[rowIndex][colIndex]];
}
printf("\nCipher text:\n%s",ct);

}

void decrypt(){
printf("%s\n",finalKey);
for(i=0;i<ptSize;i++)printf("|");
printf("\n");
printf("%s\n",pt);

for(i=0;i<ptSize;i++){

 rowIndex = finalKey[i]-97;

 for(j=0;j<26;j++){
  if(alpha[pt[i]-97]==alpha[reftable[rowIndex][j]]){
   colIndex=j;
   break;
  }
 }
 ct[i] = alpha[colIndex];
}

printf("\Plain text:\n%s",ct);

}

void printRefTable(){
//printing reference table
for(i=0;i<s;i++){
 for(j=0;j<s;j++){
  temp = reftable[i][j];
  printf("%c,",alpha[temp]);
 }
 printf("\n");
}
}
