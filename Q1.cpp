#include <stdio.h>


struct CARRECORD {
	int car_number;
	int miles_driven;
	int gallons_used;
}; // Declare the single structure type for a car record

int main() {
	struct CARRECORD cars[5]; //Declare array of five car records

	for (int i = 0; i < 5; i++) {
		printf("Enter the details of car %d:\n", i + 1);
		printf("Car number: ");
		scanf_s("%d", &cars[i].car_number);
		printf("Miles driven: ");
		scanf_s("%d", &cars[i].miles_driven);
		printf("Gallons used: ");
		scanf_s("%d", &cars[i].gallons_used);
	}
	printf("\ndata entered:\n");
	for (int i = 0; i < 5; i++) {
		printf("Car number: %d, Miles driven: %d, Gallons used: %d\n", cars[i].car_number, cars[i].miles_driven, cars[i].gallons_used);
	}

	return 0;

}