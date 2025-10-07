figure(1)
subplot(3,1,1)
plot(time,Speed_o);
title('waveform of the motor speed')
grid;
subplot(3,1,2)
plot(time,Voltage_o);
axis([1.5,1.505,-50,650])
title('waveform of the armature voltage')
xlabel('time(sec)')
grid;
subplot(3,1,3)
plot(time,Voltage_o);
%axis([3.9,3.905,-50,650])
title('waveform of the armature voltage')
xlabel('time(sec)')
grid;


figure(2)
subplot(2,1,1)
plot(time,Torque_o);
title('waveform of the motor torque')
grid;
subplot(2,1,2)
plot(time,ia_o);
title('waveform of the armature current')
xlabel('time(sec)')
grid;

figure(3)
subplot(2,1,1)
plot(time,Voltage_o);
title('zoomed waveform of the armature voltage')
axis([3.9,3.905,0,650])
grid;
subplot(2,1,2)
plot(time,ia_o);
title('zoomed waveform of the armature current')
xlabel('time(sec)')
axis([3.9,3.905,-5,5])
grid;
