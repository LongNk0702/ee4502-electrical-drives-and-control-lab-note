figure(1)
subplot(3,1,1)
plot(time,Voltage_c);
axis([0,10,-10,750])
title('Armature voltage')
xlabel('time(sec)')
grid;
subplot(3,1,2)
plot(time,Voltage_c);
%axis([1.1,3.02,0,750])
title('Zoomed waveform of armature voltage')
xlabel('time(sec)')
grid;
subplot(3,1,3)
plot(time,ia_c);
axis([1.8,2.2,-2.5,5])
title('Armature current')
xlabel('time(sec)')
grid;


figure(2)
subplot(2,1,1)
plot(time,speedref_c,time,Speed_c);
title('waveform of the reference and actual speed')
grid;
subplot(2,1,2)
plot(time,torqueref_c,time,Torque_c);
title('waveform of the reference and actual torque')
xlabel('time(sec)')
grid;