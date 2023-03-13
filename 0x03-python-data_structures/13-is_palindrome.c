#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

/* Function to find the middle node of the linked list */
struct node* findMiddle(struct node* head) {
    listint_t* slow_ptr = head;
    listint_t* fast_ptr = head;

    while(fast_ptr != NULL && fast_ptr->next != NULL) {
        fast_ptr = fast_ptr->next->next;
        slow_ptr = slow_ptr->next;
    }

    return slow_ptr;
}

/* Function to reverse the linked list */
struct node* reverseList(struct node* head) {
    listint_t* prev = NULL;
    listint_t* curr = head;
    listint_t* next = NULL;

    while(curr != NULL) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }

    return prev;
}

/* Function to check if the linked list is a palindrome */
int is_palindrome(listint_t **head) {
    listint_t* middle_node = findMiddle(head);
    listint_t* second_half = reverseList(middle_node);
    listint_t* first_half = head;

    while(second_half != NULL) {
        if(first_half->n != second_half->n) {
            return 0;
        }
        first_half = first_half->next;
        second_half = second_half->next;
    }

    return 1;
}
