% Example script for source reconstruction and parcellation
% This script takes some example data, downsamples it,
% and then calculates source reconstruction using MNE.




%% Load EEG-data
% This is pre-processed and cleaned data
testData=load('s09_Fixed1AverageDes2018.mat');
testData=testData.fixedP1;

% Downsample data

cfg=[];
cfg.latency=[-0.5 12];
dataToProcess=ft_selectdata(cfg, testData);

cfg=[];
cfg.resamplefs=250;
cfg.detrend='no';
cfg.demean='no';
cfg.trials='all';
downSampledData=ft_resampledata(cfg, dataToProcess);

% Prepare data for source reconstruction
% Noise covariance is calculated from -500 ms to 0 ms before trial start.
cfg=[];
cfg.covariance='yes';
cfg.covariancewindow=[-0.5, 0];
cfg.keeptrials='no';
testTimeLockAvg=ft_timelockanalysis(cfg, downSampledData);


%% Source reconstruction

% Load electrode layout file (included in Fieldtrip)
% This will depend on your EEG-system
load acticap-64ch-standard2

% Load head models for forward volume conduction modeling
load standard_bem

% Load the electrode positions
% This will depend on your EEG-system's layout.
elec=ft_read_sens('easycap-M1.txt');


% Re-align the electrodes with the head volume
cfg=[];
cfg.method='project';
cfg.elec=elec;
cfg.channel=testData.label;
cfg.casesensitive='no';
cfg.keepchannel='no';
cfg.headshape=vol.bnd(1);

elec_realigned=ft_electroderealign(cfg, elec);


% Inspect that the electrodes seems to match the head model.
figure;
ft_plot_mesh(vol.bnd(1), 'edgecolor','none','facealpha',0.8,'facecolor',[0.6 0.6 0.8]);
hold on;
ft_plot_sens(elec_realigned);


% Load model of the cortex (included in Fieldtrip)
sourcemodel=ft_read_headshape('cortex_5124.surf.gii');


% Make the forward solution/leadfield
cfg=[];
cfg.elec=elec_realigned;
cfg.channel='all';
cfg.headmodel=vol;
cfg.grid=sourcemodel;

leadfield=ft_prepare_leadfield(cfg);


% Setting up the parcellation
% Use AAL atlas included in Fieldtrip (change path here dependend on your
% system)
aal=ft_read_atlas('C:\Users\olehe\Desktop\MIB\General code\Toolboxes\fieldtrip-20180816\template\atlas\aal\ROI_MNI_V4.nii');

% Interpolate the AAL with the source model.
cfg=[];
cfg.parameter='tissue';
cfg.interpmethod='nearest';
sourcemodel2=ft_sourceinterpolate(cfg, aal, sourcemodel);


% Calculate the inverse solution (source reconstruction)

cfg=[];
cfg.method='mne';
cfg.channel='all';
cfg.elec=elec_realigned;
cfg.grid=leadfield;
cfg.headmodel=vol;
cfg.mne.prewhiten='yes';
cfg.mne.lambda=3;
cfg.mne.scalesourcecov='yes';
cfg.mne.keepfilter='no';
cfg.keepleadfield='no';

sourceDataAvg=ft_sourceanalysis(cfg, testTimeLockAvg);


% Parcellate the source reconstructed data according to the atlas.
cfg=[];
cfg.method='mean';
cfg.parcellation='tissue';
cfg.parameter='pow';


parcellationData=ft_sourceparcellate(cfg, sourceDataAvg, sourcemodel2);
















