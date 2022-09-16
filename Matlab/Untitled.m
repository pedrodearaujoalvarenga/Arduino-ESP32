clear all,close all, clc;
                             
N=1024;   
load('Bernoulli.mat'); % ajuste CR entre 1 a 19 para ajustar a taxa de compress?o

y=[-0.14,-0.14,-0.14,-0.14,-0.14,-0.14,-0.14,-0.155,-0.11,-0.125,-0.125,-0.125,-0.1,-0.07,-0.075,-0.025,-0.005,0.005,0.05,0.17,0.17,0.185,0.105,0.06,0.06,0.015,-0.07,-0.12,-0.12,-0.17,-0.16,-0.12,-0.14,-0.155,-0.105,-0.13,-0.14,-0.1,0.18,0.38,0.605,-0.055,-0.195,-0.125,-0.1,-0.135,-0.1,-0.125,-0.12,-0.115,-0.095,-0.095,-0.11,-0.11,-0.105,-0.09,-0.09,-0.115,-0.09,-0.085,-0.05,-0.09,-0.08,-0.06,-0.075,-0.08,-0.07,-0.055,-0.07,-0.085,-0.04,-0.065,-0.045,-0.045,-0.035,-0.02,-0.04,-0.03,-0.055,-0.065,-0.085,-0.08,-0.07,-0.08,-0.09,-0.09,-0.09,-0.105,-0.14,-0.12,0.115,-0.145,-0.15,-0.13,-0.155,-0.155,-0.155,-0.13,-0.135,-0.15,-0.155,-0.135,-0.13,-0.14,-0.165,-0.125,-0.145,-0.15,-0.16,-0.15,-0.16,-0.145,-0.15,-0.145,-0.135,-0.13,-0.15,-0.13,-0.125,-0.12,-0.13,-0.115,-0.105,-0.11,-0.115,-0.125,-0.1,-0.11,-0.1,-0.085,-0.105,-0.09,-0.11,-0.095,-0.085,-.095,-0.11,-0.1,-0.09,-0.085,-0.,-0.085,-0.075,-0.095,-0.125,-0.07,-0.06,-0.045,-0.5,0.,0.02,0.05,0.175,0.18,0.205,0.145,0.115,0.095,-0.02,-0.085,-0.1,-0.16,-0.16,-0.155,-0.145,-0.13,-0.145,-0.155,-0.145,-0.135,-0.12,-0.115,-0.115,-0.105,-0.1,-0.14,0.365,0.57,0.805,0.15,-0.175,-0.14,-0.135,-0.16,-0.13,-0.12,-0.12,-0.14,-0.12,-0.125,-0.135,-0.16,-0.11,-0.12,-0.13,-0.075,-0.075,-0.095,-0.075,-0.055,-0.055,-0.075,-0.075,-0.08,-0.07,-0.085,-0.1,-0.11,-0.1,-0.085,-0.085,-0.11,-0.12,-0.105,-0.135,-0.115,-0.095,-0.12,-0.11,-0.105,-0.125,-0.125,-0.17,-0.145,-0.185,-0.21,-0.23,-0.19,-0.195,-0.21,-0.24,-0.235,-0.21,-0.22,-0.245,-0.225,-0.22,-0.235,-0.26,-0.23,-0.23,-0.25,-0.25,-0.25,-0.26,-0.275,-0.285,-0.265,-0.255,-0.265,-0.265,-0.255,-0.265,-0.265,-0.265,-0.26,-0.27,-0.27,-0.225,-0.225,-0.265,-0.255,-0.235,-0.27,-0.25,-0.225,-0.225,-0.235,-0.245-0.24,-0.225,-0.24,-0.245,-0.245,-0.215,-0.225,-0.225,-0.2,-0.22,-0.235,-0.22,-0.205,-0.2,-0.195,-0.19,-0.175,-0.2,-0.18,-0.175,-0.195,-0.2,-0.19,-0.175,-0.18,-0.2,-0.195,-0.15,-0.15,-0.15,-0.135,-0.105,-0.08,-0.055,-0.015,0.03,0.045,-0.01,-0.025,-0.05,-0.07,-0.09,-0.145,-0.185,-0.205,-0.2,-0.2,-0.21,-0.215,-0.19,-0.19,-0.205,-0.18,-0.17,-0.165,-0.18,0.415,0.695,0.58,-0.195,-0.26,-0.25,-0.165,-0.155,-0.14,-0.195,-0.165,-0.18,-0.2,-0.175,-0.15,-0.155,-0.13,-0.12,-0.135,-0.13,-0.11,-0.115,-0.11,-0.135,-0.11,-0.125,-0.1,-0.085,-0.095,-0.1,-0.095,-0.095,-0.095,-0.085,-0.08,-0.12,-0.12,-0.105,-0.135,-0.145,-0.16,-0.135,-0.14,-0.17,-0.155,-0.175,-0.175,-0.15,-0.145,-0.155,-0.18,-0.16,-0.15,-0.155,-0.17,-0.165,-0.18,-0.185,-0.175,-0.19,-0.18,-0.175,-0.195,-0.185,-0.185,-0.17,-0.155,-0.19,-0.18,-0.16,-0.155,-0.155,-0.165,-0.165,-0.125,-0.17,-0.165,-0.15,-0.145,-0.16,-0.15,-0.145,-0.145,-0.175,0.14,-0.115,-0.135,-0.125,-0.115,-0.13,-0.15,-0.14,-0.14,-0.045,-0.06,-0.04,0.055,0.11,0.14,0.16,0.125,0.095,0.065,0.085,-0.025,-0.07,-0.095,-0.11,-0.165,-0.185,-0.15,-0.155,-0.17,-0.14,0.36,0.575,0.735,0.76,0.56,-0.23,-0.15,-0.12,-0.12,-0.17,-0.14,-0.16,-0.16,-0.16,-0.16,0.15,-0.14,-0.14,-0.155,-0.155,-0.155,-0.13,-0.125,-0.12,-0.12,-0.12,-0.125,-0.12,-0.095,-0.105,-0.1,-0.095,-0.105,0.105,-0.085,-0.095,-0.095,-0.1,-0.08,-0.105,-0.06,-0.07,-0.08,-0.045,-0.06,-0.055,-0.055,-0.045,-0.085,-0.065,-0.095,-0.1,-0.105,-0.13,-0.12,-0.105,-0.12,-0.15,-0.13,-0.13,-0.14,-0.16,-0.165,-0.15,-0.135,-0.125,-0.16,-0.16,-0.15,-0.135,-0.145,-0.1,-0.12];
y=y';

M=length(y);
CR = (N-M)/N;

Phi=BernoulliSample(1:M,:);            

   
ecgstr=['ecg1'];                 
x=cell2mat(struct2cell(load(ecgstr)));     



[ww]=dwt( N,'db2',5);
Psi=[ww];                                  
T=Phi*Psi'; 



hat_s=Alg_bp(y,T,N);    
hat_x=real(Psi'*hat_s); 
                

PRD=norm(x-hat_x)/norm(x)*100;    

fprintf( 'PRD = %.2f \n', PRD); % ideal < 9

fprintf( 'Compressao = %.0f \n', round(M/N*100));

%fprintf('CR',round(M/N*100,0));

%,'% ','......',' PRD ',num2str(round(PRD,1)) );
clf;

plot(x+1,'k','linewidth',1)
hold on

plot((hat_x-0.15),'r','linewidth',1)
plot((x-hat_x-0.9),'b', 'LineWidth',1)
set(legend('$\ {x(t)}$ ','$\hat{x}(t)$','Differenca'),'Interpreter','Latex','FontSize', 10)
set(gca,'xlim',[0 1024])
xlabel('Samples');
ylabel('Volts');
wav = 'db2'
suptitle(['Wavelet ' wav,'......', ' CR ',num2str(round(M/N*100,0)),'% ','......',' PRD ',num2str(round(PRD,1))] );