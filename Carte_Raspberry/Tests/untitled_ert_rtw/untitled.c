/*
 * Classroom License -- for classroom instructional use only.  Not for
 * government, commercial, academic research, or other organizational use.
 *
 * File: untitled.c
 *
 * Code generated for Simulink model 'untitled'.
 *
 * Model version                  : 1.0
 * Simulink Coder version         : 9.3 (R2020a) 18-Nov-2019
 * C/C++ source code generated on : Tue Feb 27 11:57:32 2024
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "untitled.h"
#include "untitled_private.h"

/* Block signals (default storage) */
B_untitled_T untitled_B;

/* Block states (default storage) */
DW_untitled_T untitled_DW;

/* Real-time model */
RT_MODEL_untitled_T untitled_M_;
RT_MODEL_untitled_T *const untitled_M = &untitled_M_;

/* Forward declaration for local functions */
static void untitled_SystemCore_release(const codertarget_linux_blocks_SDLV_T
  *obj);
static void untitled_SystemCore_delete_b(const codertarget_linux_blocks_SDLV_T
  *obj);
static void matlabCodegenHandle_matlabCod_b(codertarget_linux_blocks_SDLV_T *obj);
static void matlabCodegenHandle_matlabCodeg(codertarget_raspi_internal_LE_T *obj);
static void rate_monotonic_scheduler(void);

/*
 * Set which subrates need to run this base step (base rate always runs).
 * This function must be called prior to calling the model step function
 * in order to "remember" which rates need to run this base step.  The
 * buffering of events allows for overlapping preemption.
 */
void untitled_SetEventsForThisBaseStep(boolean_T *eventFlags)
{
  /* Task runs when its counter is zero, computed via rtmStepTask macro */
  eventFlags[1] = ((boolean_T)rtmStepTask(untitled_M, 1));
}

/*
 *   This function updates active task flag for each subrate
 * and rate transition flags for tasks that exchange data.
 * The function assumes rate-monotonic multitasking scheduler.
 * The function must be called at model base rate so that
 * the generated code self-manages all its subrates and rate
 * transition flags.
 */
static void rate_monotonic_scheduler(void)
{
  /* Compute which subrates run during the next base time step.  Subrates
   * are an integer multiple of the base rate counter.  Therefore, the subtask
   * counter is reset when it reaches its limit (zero means run).
   */
  (untitled_M->Timing.TaskCounters.TID[1])++;
  if ((untitled_M->Timing.TaskCounters.TID[1]) > 4) {/* Sample time: [0.5s, 0.0s] */
    untitled_M->Timing.TaskCounters.TID[1] = 0;
  }
}

real_T rt_roundd_snf(real_T u)
{
  real_T y;
  if (fabs(u) < 4.503599627370496E+15) {
    if (u >= 0.5) {
      y = floor(u + 0.5);
    } else if (u > -0.5) {
      y = u * 0.0;
    } else {
      y = ceil(u - 0.5);
    }
  } else {
    y = u;
  }

  return y;
}

static void untitled_SystemCore_release(const codertarget_linux_blocks_SDLV_T
  *obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_SDL_videoDisplayTerminate(0, 0);
  }
}

static void untitled_SystemCore_delete_b(const codertarget_linux_blocks_SDLV_T
  *obj)
{
  untitled_SystemCore_release(obj);
}

static void matlabCodegenHandle_matlabCod_b(codertarget_linux_blocks_SDLV_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    untitled_SystemCore_delete_b(obj);
  }
}

static void matlabCodegenHandle_matlabCodeg(codertarget_raspi_internal_LE_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
  }
}

/* Model step function for TID0 */
void untitled_step0(void)              /* Sample time: [0.1s, 0.0s] */
{
  {                                    /* Sample time: [0.1s, 0.0s] */
    rate_monotonic_scheduler();
  }

  /* S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
  MW_videoCaptureOutput(untitled_ConstP.V4L2VideoCapture_p1,
                        untitled_B.V4L2VideoCapture_o1,
                        untitled_B.V4L2VideoCapture_o2,
                        untitled_B.V4L2VideoCapture_o3);

  /* MATLABSystem: '<S1>/MATLAB System' */
  memcpy(&untitled_B.pln1[0], &untitled_B.V4L2VideoCapture_o1[0], 76800U *
         sizeof(uint8_T));
  memcpy(&untitled_B.pln2[0], &untitled_B.V4L2VideoCapture_o2[0], 76800U *
         sizeof(uint8_T));
  memcpy(&untitled_B.pln3[0], &untitled_B.V4L2VideoCapture_o3[0], 76800U *
         sizeof(uint8_T));
  MW_SDL_videoDisplayOutput(untitled_B.pln1, untitled_B.pln2, untitled_B.pln3);

  /* External mode */
  rtExtModeUploadCheckTrigger(2);
  rtExtModeUpload(0, (real_T)untitled_M->Timing.taskTime0);

  /* signal main to stop simulation */
  {                                    /* Sample time: [0.1s, 0.0s] */
    if ((rtmGetTFinal(untitled_M)!=-1) &&
        !((rtmGetTFinal(untitled_M)-untitled_M->Timing.taskTime0) >
          untitled_M->Timing.taskTime0 * (DBL_EPSILON))) {
      rtmSetErrorStatus(untitled_M, "Simulation finished");
    }

    if (rtmGetStopRequested(untitled_M)) {
      rtmSetErrorStatus(untitled_M, "Simulation finished");
    }
  }

  /* Update absolute time */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   */
  untitled_M->Timing.taskTime0 =
    ((time_T)(++untitled_M->Timing.clockTick0)) * untitled_M->Timing.stepSize0;
}

/* Model step function for TID1 */
void untitled_step1(void)              /* Sample time: [0.5s, 0.0s] */
{
  real_T tmp;
  uint8_T tmp_0;
  static const char_T tmp_1[69] = { 'I', 'n', 'v', 'a', 'l', 'i', 'd', ' ', 'L',
    'E', 'D', ' ', 'v', 'a', 'l', 'u', 'e', '.', ' ', 'L', 'E', 'D', ' ', 'v',
    'a', 'l', 'u', 'e', ' ', 'm', 'u', 's', 't', ' ', 'b', 'e', ' ', 'a', ' ',
    'l', 'o', 'g', 'i', 'c', 'a', 'l', ' ', 'v', 'a', 'l', 'u', 'e', ' ', '(',
    't', 'r', 'u', 'e', ' ', 'o', 'r', ' ', 'f', 'a', 'l', 's', 'e', ')', '.' };

  static const char_T tmp_2[5] = "none";
  char_T tmp_3[5];
  int32_T i;

  /* DiscretePulseGenerator: '<Root>/Pulse Generator' */
  untitled_B.PulseGenerator = (untitled_DW.clockTickCounter <
    untitled_P.PulseGenerator_Duty) && (untitled_DW.clockTickCounter >= 0) ?
    untitled_P.PulseGenerator_Amp : 0.0;
  if (untitled_DW.clockTickCounter >= untitled_P.PulseGenerator_Period - 1.0) {
    untitled_DW.clockTickCounter = 0;
  } else {
    untitled_DW.clockTickCounter++;
  }

  /* End of DiscretePulseGenerator: '<Root>/Pulse Generator' */

  /* MATLABSystem: '<Root>/LED' */
  if ((untitled_B.PulseGenerator == 0.0) || (untitled_B.PulseGenerator == 1.0))
  {
  } else {
    memcpy(&untitled_B.cv[0], &tmp_1[0], 69U * sizeof(char_T));
    perror(untitled_B.cv);
  }

  for (i = 0; i < 5; i++) {
    tmp_3[i] = tmp_2[i];
  }

  EXT_LED_setTrigger(0U, tmp_3);
  tmp = rt_roundd_snf(untitled_B.PulseGenerator);
  if (tmp < 256.0) {
    if (tmp >= 0.0) {
      tmp_0 = (uint8_T)tmp;
    } else {
      tmp_0 = 0U;
    }
  } else {
    tmp_0 = MAX_uint8_T;
  }

  EXT_LED_write(0U, tmp_0);

  /* End of MATLABSystem: '<Root>/LED' */
  rtExtModeUpload(1, (real_T)((untitled_M->Timing.clockTick1) * 0.5));

  /* Update absolute time */
  /* The "clockTick1" counts the number of times the code of this task has
   * been executed. The resolution of this integer timer is 0.5, which is the step size
   * of the task. Size of "clockTick1" ensures timer will not overflow during the
   * application lifespan selected.
   */
  untitled_M->Timing.clockTick1++;
}

/* Model step wrapper function for compatibility with a static main program */
void untitled_step(int_T tid)
{
  switch (tid) {
   case 0 :
    untitled_step0();
    break;

   case 1 :
    untitled_step1();
    break;

   default :
    break;
  }
}

/* Model initialize function */
void untitled_initialize(void)
{
  /* Registration code */
  rtmSetTFinal(untitled_M, 100.0);
  untitled_M->Timing.stepSize0 = 0.1;

  /* External mode info */
  untitled_M->Sizes.checksums[0] = (2617486005U);
  untitled_M->Sizes.checksums[1] = (727500150U);
  untitled_M->Sizes.checksums[2] = (3293938340U);
  untitled_M->Sizes.checksums[3] = (261262141U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[4];
    untitled_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    systemRan[1] = &rtAlwaysEnabled;
    systemRan[2] = &rtAlwaysEnabled;
    systemRan[3] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(untitled_M->extModeInfo,
      &untitled_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(untitled_M->extModeInfo, untitled_M->Sizes.checksums);
    rteiSetTPtr(untitled_M->extModeInfo, rtmGetTPtr(untitled_M));
  }

  {
    static const char_T tmp[5] = "none";
    char_T tmp_0[5];
    int32_T i;

    /* Start for S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
    MW_videoCaptureInit(untitled_ConstP.V4L2VideoCapture_p1, 0, 0, 0, 0, 320U,
                        240U, 2U, 2U, 1U, 0.1);

    /* Start for MATLABSystem: '<S1>/MATLAB System' */
    untitled_DW.obj.matlabCodegenIsDeleted = false;
    untitled_DW.obj.isInitialized = 1;
    untitled_DW.obj.PixelFormatEnum = 1;
    MW_SDL_videoDisplayInit(untitled_DW.obj.PixelFormatEnum, 1, 1, 320.0, 240.0);
    untitled_DW.obj.isSetupComplete = true;

    /* End of SystemInitialize for SubSystem: '<Root>/SDL Video Display' */

    /* Start for MATLABSystem: '<Root>/LED' */
    untitled_DW.obj_p.matlabCodegenIsDeleted = false;
    untitled_DW.obj_p.isInitialized = 1;
    for (i = 0; i < 5; i++) {
      tmp_0[i] = tmp[i];
    }

    EXT_LED_setTrigger(0U, tmp_0);
    untitled_DW.obj_p.isSetupComplete = true;

    /* End of Start for MATLABSystem: '<Root>/LED' */
  }
}

/* Model terminate function */
void untitled_terminate(void)
{
  /* Terminate for S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
  MW_videoCaptureTerminate(untitled_ConstP.V4L2VideoCapture_p1);

  /* Terminate for MATLABSystem: '<S1>/MATLAB System' */
  matlabCodegenHandle_matlabCod_b(&untitled_DW.obj);

  /* Terminate for MATLABSystem: '<Root>/LED' */
  matlabCodegenHandle_matlabCodeg(&untitled_DW.obj_p);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
