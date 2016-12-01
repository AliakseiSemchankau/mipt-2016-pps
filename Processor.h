/**
 * @(#) Processor.h
 */

#ifndef PROCESSOR_H_H
#define PROCESSOR_H_H

#include "Sub task.h"
class Processor
{
	
public:
	int isBusy;
	
	
private:
	void executeSubTask( );
	Sub_task * stasks;
	
	
};

#endif
