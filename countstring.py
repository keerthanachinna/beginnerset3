 importnumpy
 x=numpy.zero((n,m))
alphabets = digits = others = i=count= 0;
    printf("Enter any string : ")
    
    while(str[i]!='\0'):    {
        if((str[i]>='a' and str[i]<='z')or(str[i]>='A' and str[i]<='Z')):
       alphabets++;
         elif(str[i]>='0' and str[i]<='9'):
       digits++;
       count++;
   printf("Alphabets = %d\n", alphabets);
    printf("Digits = %d\n", digits);
   return 0;

