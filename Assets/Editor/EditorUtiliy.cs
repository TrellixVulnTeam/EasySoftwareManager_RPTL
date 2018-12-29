﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.Linq;

public class LayooutWindow : EditorWindow {

    private bool unfolded = true;
    private Transform[] selecteds;

    private void OnGUI()
    {

        selecteds = Selection.transforms;


        if (selecteds != null && selecteds.Length > 1)
        {
            GUILayout.Space(10);
            GUILayout.Label("物体拖拽");
            if (GUILayout.Button("生成父拖拽物体"))
            {
                CreateParentForDrag();
            }

            //if (GUILayout.Button("移除父拖拽物体"))
            //{
            //    RemoveParentForDrag();
            //}


            //排列
            GUILayout.Space(10);
            GUILayout.Label("物体排序");
            if (GUILayout.Button("开始x轴排列"))
            {
                LayoutByAxisX();
            }

            if (GUILayout.Button("开始y轴排列"))
            {
                LayoutByAxisY();
            }

            if (GUILayout.Button("开始z轴排列"))
            {
                LayoutByAxisZ();
            }

            if (GUILayout.Button("开始三轴排列"))
            {
                LayoutByAxisX();
                LayoutByAxisY();
                LayoutByAxisZ();
            }
        }
    }

    private void RemoveParentForDrag()
    {
        //Transform originParent = selecteds[0].parent.parent;
        //Transform tempParent = selecteds[0].parent;
        //foreach (Transform item in tempParent.transform)
        //{
        //    item.SetParent(originParent);
        //}
        //GameObject.DestroyImmediate(tempParent.gameObject);
    }

    private void CreateParentForDrag()
    {
        //多物体拖拽
        Transform originParent;
        Vector3 temp = Vector3.zero;
        for (int i = 0; i < selecteds.Length; i++)
        {
            temp += selecteds[i].position;
        }
        Vector3 center = temp / selecteds.Length;
        originParent = selecteds[0].parent;

        GameObject parent = new GameObject("dragParent");
        parent.transform.position = center;
        parent.transform.localScale = Vector3.one;
        parent.transform.SetParent(originParent);
        for (int i = 0; i < selecteds.Length; i++)
        {
            selecteds[i].SetParent(parent.transform);
        }
    }

    private void LayoutByAxisZ()
    {
        var trans = selecteds.OrderBy(n => n.position.z);
        Transform deepest = trans.First();
        Transform forest = trans.Last();
        float space_z = (forest.position.z - deepest.position.z) / (selecteds.Length - 1);

        int index = 0;
        foreach (var item in trans)
        {
            item.position = new Vector3(item.position.x, item.position.y, deepest.position.z + space_z * index);
            index++;
        }
    }

    private void LayoutByAxisY()
    {
        var trans = selecteds.OrderBy(n => n.position.y);
        Transform bottom = trans.First();
        Transform top = trans.Last();
        float space_y = (top.position.y - bottom.position.y) / (selecteds.Length - 1);

        int index = 0;
        foreach (var item in trans)
        {
            item.position = new Vector3(item.position.x, bottom.position.y + space_y * index, item.position.z);
            index++;
        }
    }

    private void LayoutByAxisX()
    {
        var trans = selecteds.OrderBy(n => n.position.x);
        Transform left = trans.First();
        Transform right = trans.Last();
        float space_x = (right.position.x - left.position.x) / (selecteds.Length - 1);

        int index = 0;
        foreach (var item in trans)
        {
            item.position = new Vector3(left.position.x + space_x * index, item.position.y, item.position.z);
            index++;
        }
    }

    private void OnInspectorUpdate()
    {
        // 重新绘制
        this.Repaint();
    }

    [MenuItem("工具/对齐工具")]
    private static void ShowWindow()
    {
        // 获取自定义窗口的实例并显示窗口
        GetWindow<LayooutWindow>().Show();
    }
}