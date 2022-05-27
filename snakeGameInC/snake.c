#include "snake.h"

void setSnake(SNAKE* s,int x, int y, int dir){
	s->size=6;
	s->ateFood=false;
	s->dir=RIGHT;
	s->pontos=malloc(sizeof(LPonto));
	s->pontos->x=x;
	s->pontos->y=y;
	s->pontos->next=malloc(sizeof(LPonto));
	LPonto aux=s->pontos->next;
	for(int i=1; i<6; i++){
		aux->x=x-i;
		aux->y=y;
		aux->next=malloc(sizeof(LPonto));
		aux = aux->next;
	}
	aux=NULL;
}

void updateSnake(SNAKE* s){
	LPonto aux=malloc(sizeof(LPonto));;
	aux->x=s->pontos->x;
	aux->y=s->pontos->y;
	aux->next=s->pontos;
	s->pontos=aux;
	if(s->dir==UP){
		s->pontos->y--;
	}
	else if(s->dir==DOWN){
		s->pontos->y++;
	}
	else if(s->dir==LEFT){
		s->pontos->x--;
	}
	else{
		s->pontos->x++;
	}
	if(!s->ateFood){

		LPonto n = aux;
		while(n->next->next!=NULL){ 
			n=n->next; 
		}
		n->next=NULL;

	}
	else{
		s->size++;
		s->ateFood=false;
	}
}

bool snakeDead(SNAKE* s,int m,int n){
	LPonto p1 = s->pontos;
	LPonto p2;
	while(p1->next!=NULL){
		p2=p1->next;
		while(p2!=NULL){
			if(p1->x%(n-2) == p2->x%(n-2) && p1->y%(m-2) == p2->y%(m-2)){
				return true;
			}
			p2=p2->next;
		}
		p1=p1->next;
	}
	return false;
}

void snakeAte(SNAKE* s, FOOD* f,int m,int n){
	if((s->pontos->x%(n-2))+1==f->y&&(s->pontos->y%(m-2))+1==f->x){
		s->ateFood=true;
		createFood(f,s,m,n);
	}
}

bool isInSnake(LPonto s, FOOD* f,int m,int n){
	LPonto aux = s;
	while(aux!=NULL){
		if((aux->x%(n-2))+1 == f->y && (aux->y%(m-2))+1==f->x){
			return true;
		}
		aux=aux->next;
	}
	return false;
}

void createFood(FOOD* f,SNAKE* s,int m,int n){
	f->x=rand()%(m-2)+1;
	f->y=rand()%(n-2)+1;
	while(isInSnake(s->pontos,f,m,n)){
		f->x=rand()%(m-2)+1;
		f->y=rand()%(n-2)+1;
	}
}

void increaseSpeed(SNAKE* s,float* time){
	*time=0.1-((s->size/3)*0.005);
}