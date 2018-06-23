int sumList( int theList[], int size )
{
	int sum = 0;
	int i = 0;
	while( i < size ) {
		sum += theList[ i ];
		i += 1;
	}
	return sum;
}
