#include "lists.h"
/**
 * check_cycle - Checks if there is a loop in a linked list.
 * @list: pointer to linked list.
 * Return: returns 1 if there is a loop and 0 if there isn't.
 */
int check_cycle(listint_t *list)
{
	listint_t *uno = NULL;
	listint_t *dos = NULL;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	if (list != NULL || list->next != NULL)
	{
		uno = list->next;
		dos = list->next->next;

		while (uno && dos && dos->next)
		{
			if (uno == dos)
			{
				return (1);
			}
			uno = uno->next;
			dos = dos->next->next;
		}
	}
	return (0);
}
