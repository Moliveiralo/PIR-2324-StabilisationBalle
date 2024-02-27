/*
 * Classroom License -- for classroom instructional use only.  Not for
 * government, commercial, academic research, or other organizational use.
 *
 * File: cameraTest.c
 *
 * Code generated for Simulink model 'cameraTest'.
 *
 * Model version                  : 1.5
 * Simulink Coder version         : 9.3 (R2020a) 18-Nov-2019
 * C/C++ source code generated on : Tue Feb 27 14:46:09 2024
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: ARM Compatible->ARM Cortex
 * Code generation objectives: Unspecified
 * Validation result: Not run
 */

#include "cameraTest.h"
#include "cameraTest_private.h"

/* Block signals (default storage) */
B_cameraTest_T cameraTest_B;

/* Block states (default storage) */
DW_cameraTest_T cameraTest_DW;

/* Real-time model */
RT_MODEL_cameraTest_T cameraTest_M_;
RT_MODEL_cameraTest_T *const cameraTest_M = &cameraTest_M_;

/* Forward declaration for local functions */
static void cameraTest_SystemCore_release(const codertarget_linux_blocks_SDLV_T *
  obj);
static void cameraTest_SystemCore_delete(const codertarget_linux_blocks_SDLV_T
  *obj);
static void matlabCodegenHandle_matlabCodeg(codertarget_linux_blocks_SDLV_T *obj);
static void cameraTest_SystemCore_release(const codertarget_linux_blocks_SDLV_T *
  obj)
{
  if ((obj->isInitialized == 1) && obj->isSetupComplete) {
    MW_SDL_videoDisplayTerminate(0, 0);
  }
}

static void cameraTest_SystemCore_delete(const codertarget_linux_blocks_SDLV_T
  *obj)
{
  cameraTest_SystemCore_release(obj);
}

static void matlabCodegenHandle_matlabCodeg(codertarget_linux_blocks_SDLV_T *obj)
{
  if (!obj->matlabCodegenIsDeleted) {
    obj->matlabCodegenIsDeleted = true;
    cameraTest_SystemCore_delete(obj);
  }
}

/* Model step function */
void cameraTest_step(void)
{
  /* S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
  MW_videoCaptureOutput(cameraTest_ConstP.V4L2VideoCapture_p1,
                        cameraTest_B.V4L2VideoCapture_o1,
                        cameraTest_B.V4L2VideoCapture_o2,
                        cameraTest_B.V4L2VideoCapture_o3);

  /* MATLABSystem: '<S1>/MATLAB System' */
  memcpy(&cameraTest_B.pln1[0], &cameraTest_B.V4L2VideoCapture_o1[0], 76800U *
         sizeof(uint8_T));
  memcpy(&cameraTest_B.pln2[0], &cameraTest_B.V4L2VideoCapture_o2[0], 76800U *
         sizeof(uint8_T));
  memcpy(&cameraTest_B.pln3[0], &cameraTest_B.V4L2VideoCapture_o3[0], 76800U *
         sizeof(uint8_T));
  MW_SDL_videoDisplayOutput(cameraTest_B.pln1, cameraTest_B.pln2,
    cameraTest_B.pln3);

  /* External mode */
  rtExtModeUploadCheckTrigger(1);

  {                                    /* Sample time: [0.1s, 0.0s] */
    rtExtModeUpload(0, (real_T)cameraTest_M->Timing.taskTime0);
  }

  /* signal main to stop simulation */
  {                                    /* Sample time: [0.1s, 0.0s] */
    if ((rtmGetTFinal(cameraTest_M)!=-1) &&
        !((rtmGetTFinal(cameraTest_M)-cameraTest_M->Timing.taskTime0) >
          cameraTest_M->Timing.taskTime0 * (DBL_EPSILON))) {
      rtmSetErrorStatus(cameraTest_M, "Simulation finished");
    }

    if (rtmGetStopRequested(cameraTest_M)) {
      rtmSetErrorStatus(cameraTest_M, "Simulation finished");
    }
  }

  /* Update absolute time for base rate */
  /* The "clockTick0" counts the number of times the code of this task has
   * been executed. The absolute time is the multiplication of "clockTick0"
   * and "Timing.stepSize0". Size of "clockTick0" ensures timer will not
   * overflow during the application lifespan selected.
   */
  cameraTest_M->Timing.taskTime0 =
    ((time_T)(++cameraTest_M->Timing.clockTick0)) *
    cameraTest_M->Timing.stepSize0;
}

/* Model initialize function */
void cameraTest_initialize(void)
{
  /* Registration code */
  rtmSetTFinal(cameraTest_M, 10.0);
  cameraTest_M->Timing.stepSize0 = 0.1;

  /* External mode info */
  cameraTest_M->Sizes.checksums[0] = (4288563262U);
  cameraTest_M->Sizes.checksums[1] = (3180772960U);
  cameraTest_M->Sizes.checksums[2] = (2702090819U);
  cameraTest_M->Sizes.checksums[3] = (3414745026U);

  {
    static const sysRanDType rtAlwaysEnabled = SUBSYS_RAN_BC_ENABLE;
    static RTWExtModeInfo rt_ExtModeInfo;
    static const sysRanDType *systemRan[3];
    cameraTest_M->extModeInfo = (&rt_ExtModeInfo);
    rteiSetSubSystemActiveVectorAddresses(&rt_ExtModeInfo, systemRan);
    systemRan[0] = &rtAlwaysEnabled;
    systemRan[1] = &rtAlwaysEnabled;
    systemRan[2] = &rtAlwaysEnabled;
    rteiSetModelMappingInfoPtr(cameraTest_M->extModeInfo,
      &cameraTest_M->SpecialInfo.mappingInfo);
    rteiSetChecksumsPtr(cameraTest_M->extModeInfo, cameraTest_M->Sizes.checksums);
    rteiSetTPtr(cameraTest_M->extModeInfo, rtmGetTPtr(cameraTest_M));
  }

  /* Start for S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
  MW_videoCaptureInit(cameraTest_ConstP.V4L2VideoCapture_p1, 0, 0, 0, 0, 320U,
                      240U, 2U, 2U, 1U, 0.1);

  /* Start for MATLABSystem: '<S1>/MATLAB System' */
  cameraTest_DW.obj.matlabCodegenIsDeleted = false;
  cameraTest_DW.obj.isInitialized = 1;
  cameraTest_DW.obj.PixelFormatEnum = 1;
  MW_SDL_videoDisplayInit(cameraTest_DW.obj.PixelFormatEnum, 1, 1, 320.0, 240.0);
  cameraTest_DW.obj.isSetupComplete = true;

  /* End of SystemInitialize for SubSystem: '<Root>/SDL Video Display' */
}

/* Model terminate function */
void cameraTest_terminate(void)
{
  /* Terminate for S-Function (v4l2_video_capture_sfcn): '<Root>/V4L2 Video Capture' */
  MW_videoCaptureTerminate(cameraTest_ConstP.V4L2VideoCapture_p1);

  /* Terminate for MATLABSystem: '<S1>/MATLAB System' */
  matlabCodegenHandle_matlabCodeg(&cameraTest_DW.obj);
}

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
