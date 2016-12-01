/**
 * @(#) Task.h
 */

#ifndef TASK_H_H
#define TASK_H_H

#include "Sub task.h"
#include "User.h"
class Task
{
	
public:
	int result;
	
	
private:
	Sub_task * tasks;
	
	User * users;
	
	
};

#endif
#include "Sub task.h"
#include "User.h"

class Task
{
	public:
	int result;
	private:
	Sub_task * tasks;
	
	User * users;
	
};
