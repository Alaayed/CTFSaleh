#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct pair {
	short s;
	short e;
} typedef pair_t;

char* longestPalindrome(char* s) {
	unsigned short len = strlen(s);
	if (len == 0) return "";

	// Create the 2D array
	pair_t **pairs = malloc(len * sizeof(pair_t *));
	for (unsigned short i = 0; i < len; i++) {
		pairs[i] = malloc((len - i) * sizeof(pair_t));
		for (unsigned short j = 0; j < len - i; j++) {
			pairs[i][j].s = -1;
			pairs[i][j].e = -1;
		}
	}

	// Base case
	pair_t largest_pair = {0, 0};
	for (int i = 0; i < len; i++) {
		pairs[0][i].s = i;
		pairs[0][i].e = i;
		if (i - 1 >= 0 && s[i] == s[i - 1]) {
			pairs[1][i - 1].s = i - 1;
			pairs[1][i - 1].e = i;
			largest_pair.s = i - 1;
			largest_pair.e = i;
		}
	}

	// Construct remaining cases
	for (int l = 2; l < len; l++) { // l = length of substring - 1
		pair_t *prev = pairs[l - 2];
		for (int i = 0; i < len - l; i++) {
			short start = prev[i + 1].s;
			short end = prev[i + 1].e;
			if (start != -1 && end != -1 && start - 1 >= 0 && end + 1 < len && s[start - 1] == s[end + 1]) {
				pairs[l][i].s = start - 1;
				pairs[l][i].e = end + 1;
				if ((end + 1) - (start - 1) > largest_pair.e - largest_pair.s) {
					largest_pair = pairs[l][i];
				}
			}
		}
	}

	// Extract the substring
	int final_len = largest_pair.e - largest_pair.s + 1;
	char* result = malloc(final_len + 1);
	strncpy(result, s + largest_pair.s, final_len);
	result[final_len] = '\0';

	// Free memory
	for (unsigned short i = 0; i < len; i++) {
		free(pairs[i]);
	}
	free(pairs);

	return result;
}
