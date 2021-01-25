void main()
{
int a[5];
int i,j,t;
clrscr();
printf("Enter array : ");
for(i=0;i<=4;i++)
{
	scanf("%d",&a[i]);
}
for(i=0;i<=3;i++)
{
	for(j=i+1;j<=4;j++)
	{
		if(a[i] > a[j])
		{
			t = a[i];
			a[] = a[j];
			a[j] = t;
		}
	}
}
printf("after sorting\n");
for(i=0;i<=4;i++)
{
	printf("%d\n",a[i]);
}
getch();
}